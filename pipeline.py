#!/usr/bin/python
from collections import deque
from instr_models import HLTInstruction, RInstruction, IInstruction, JInstruction, Nop
import struct, binascii

class PipelineSim(object):
    def __init__(self, memory, instrs):
        self.instr_count = 0
        self.cycle_count = 0
        self.registers = [0 for i in range(32)]
        self.memory = memory
        self.pc = 0x00001000
        self.instructions = instrs
        self.pipeline = deque([Nop for i in range(5)])

    def __str__(self):
        result = 'REGISTER CONTENT\n'
        for i in range(0,len(self.registers),2):
            reg0 = self.registers[i]
            reg1 = self.registers[i+1]
            result += 'R%s: 0x%08x R%s: 0x%08x\n' % (i, reg0, i+1, reg1)

#        result += '\nMEMORY CONTENT\n'
#        i = 1
#        mem_addresses = sorted(self.memory.keys())
#        for addr in mem_addresses[:32]:
#            packed = struct.pack('@I',self.memory[addr])
#            h = binascii.hexlify(packed)
#            if i == 1:
#                result += '0x%08x %s %s %s %s ' % (addr,h[:2],h[2:4],h[4:6],h[6:])
#                i += 1
#            elif i == 4:
#                result += '%s %s %s %s\n' % (h[:2],h[2:4],h[4:6],h[6:])
#                i = 1
#            else:
#                result += '%s %s %s %s ' % (h[:2],h[2:4],h[4:6],h[6:])
#                i += 1
        return result

    def find_instr(self,addr):
        """ Returns the instruction at the given address """
        f = lambda i: i.addr == addr
        match = filter(f,self.instructions)
        return match[0]

    def advance(self):
        """ Moves the clock a single tick """
        empty_pipe = deque([Nop for i in range(5)])
        while True:
#            if self.cycle_count == 1 or self.cycle_count == 9:
#                print "*** Cycle # %s content ***\n" % self.cycle_count
#                print self
            try:
                instr = self.find_instr(self.pc)
                self.do_stages(instr)
            except IndexError:
                self.do_stages(Nop)
            if type(self.pipeline[0]) is HLTInstruction:
                break

        # flushes the pipeline after we see an HLT
        while self.pipeline != empty_pipe:
            self.do_stages(Nop)


    # takes instr as an argument so we can fetch Nops
    def do_stages(self, instr):
        self.write(self.pipeline[4])
        self.access_mem(self.pipeline[3])
        self.execute(self.pipeline[2])
        self.decode(self.pipeline[1])
        self.fetch(instr)
        print '\n'
        self.cycle_count += 1

    def fetch(self, instr):
        print 'Adding %s to the pipeline...' % instr
        if (len(self.pipeline) >= 5):
            self.pipeline.pop()
        self.pipeline.appendleft(instr)
        if instr is not Nop:
            self.instr_count += 1
        self.pc += 4

    def decode(self, instr):
        print 'Decoding %s...' % instr
        pass

    def execute(self, instr):
        print 'Executing %s...' % instr
        # TODO: hazard detection and forwarding
        # TODO: write more logic to update instr.unwritten with registers
        if instr is not Nop and type(instr) is not HLTInstruction:
            i = instr.instr
            c_sigs = instr.c_signals
            if c_sigs['RegWrite']:
                dest = instr.rd if c_sigs['RegDst'] else instr.rt
                instr.unwritten.append(dest)

            if i == 'beq':
                val1 = self.registers[instr.rs]
                val2 = self.registers[instr.rt]
                if val1 == val2:
                    # not sure if this is the complete math, might involve subtraction
                    self.pc += 4 + (4*instr.imm)
                    self.pipeline[1] = Nop
                    self.pipeline[0] = Nop
            elif i == 'j':
                self.pc = instr.target
                self.pipeline[1] = Nop
                self.pipeline[0] = Nop
            else:
                val1 = self.registers[instr.rs]
                val2 = self.registers[instr.rt] if not c_sigs['ALUSrc'] else instr.imm
                instr.result = eval('%s+%s' % (val1,val2))
                print '\tinstr: %s -- %s,%s' % (instr,val1,val2)

    def access_mem(self, instr):
        print 'Access memory with %s (if needed)...' % instr
        # sw : M[R[rs]+SignExtImm] = R[rt]
        # lw : R[rt] = M[R[rs]+SignExtImm] 
        if instr is Nop:
            pass
        elif instr.instr == 'sw':
            self.memory[instr.result] = self.registers[instr.rt]
        elif instr.instr == 'lw':
            offset = instr.result
            instr.result = self.memory[offset]
            print '\toffset: %s; result: %s' % (offset,instr.result)
        else:
            pass 

    def write(self, instr):
        print 'Writing back with %s...' % instr
        if instr is Nop or type(instr) is HLTInstruction:
            pass
        elif instr.c_signals['RegWrite']:
            if instr.result is not None:
                dest = instr.rd if instr.c_signals['RegDst'] else instr.rt
                self.registers[dest] = instr.result
                if dest in instr.unwritten:
                    instr.unwritten.remove(dest)
        else:
            pass
