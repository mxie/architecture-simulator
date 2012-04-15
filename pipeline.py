#!/usr/bin/python
from collections import deque
from instr_models import HLTInstruction, RInstruction, IInstruction, JInstruction, Nop

class PipelineSim(object):
    def __init__(self, memory, instrs):
        self.instr_count = 0
        self.cycle_count = 0
        self.registers = [0 for i in range(32)]
        self.memory = memory 
        self.pc = 0x00001000
        self.instructions = deque(instrs)
        self.pipeline = deque([Nop for i in range(5)])

    def __str__(self):
        result = 'REGISTER CONTENT\n'
        for i in range(0,len(self.registers),2):
            reg0 = self.registers[i]
            reg1 = self.registers[i+1]
            result += 'R%s: 0x%08x R%s: 0x%08x\n' % (i, reg0, i+1, reg1)

        result += '\nMEMORY CONTENT\n'
        i = 1
        mem_addresses = sorted(self.memory.keys())
        for addr in mem_addresses[:32]:
            data = self.memory[addr]
            h = '%s' % data if data != 0 else '%08x' % data
            if (i == 1):
                result += '0x%08x %s %s %s %s ' % (addr,h[:2],h[2:4],h[4:6],h[6:])
                i += 1
            elif (i == 4):
                result += '%s %s %s %s\n' % (h[:2],h[2:4],h[4:6],h[6:])
                i = 1
            else:
                result += '%s %s %s %s ' % (h[:2],h[2:4],h[4:6],h[6:])
                i += 1
        return result

    def advance(self):
        empty_pipe = deque([Nop for i in range(5)])
        while True:
            # I forget when she wanted us to print 'snapshots' of our stuff,
            # was it after
            if self.cycle_count == 1 or self.cycle_count == 9:
                print "*** Cycle # %s content ***\n" % self.cycle_count
                print self
            try:
                self.do_stages(self.instructions.popleft())
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
        self.cycle_count += 1

    def fetch(self, instr):
        if (len(self.pipeline) >= 5):
            self.pipeline.pop()
        self.pipeline.appendleft(instr)
        if instr is not Nop:
            self.instr_count += 1

    def decode(self, instr):
        # add stuff to represent stuff as ints and not binary for when we
        # throw stuff into the registers
        # (to make it easier to add, addi, etc with ints instead of binary stuff)
        pass

    def execute(self, instr):
        if instr is Nop:
            pass
        else:
            pass
            # a bunch of stuff here

    def access_mem(self, instr):
        if instr is Nop:
            pass
        elif instr.instr == 'lw' or instr.instr == 'sw':
            # DO STUFF HERE if lw or sw!
            print "hi"
        else:
            pass

    def write(self, instr):
        if instr is Nop or type(instr) is JInstruction:
            pass
        else:
            if instr.result is not None:
                self.registers[int(instr.rd)] = instr.result
            else:
                pass