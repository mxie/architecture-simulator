#!/usr/bin/python

# Melissa Xie, Courtney Sims
# EECE 3230 Final Project
# Prof. Fei, April 2012

from collections import deque
from instruction import HLTInstruction, RInstruction, IInstruction, JInstruction, Nop
import struct, binascii

class PipelineSim(object):
    def __init__(self, memory, instrs):
        """Initializes this pipeline."""
        self.instr_count = 0
        self.cycle_count = 0
        self.registers = [0 for i in range(32)]
        self.memory = memory
        self.pc = 0x00001000
        self.instructions = instrs
        self.pipeline = deque([Nop for i in range(5)])
        self.stall = False
        self.hazards = []
        self.use_instr = None
        self.branched = False

    def __str__(self):
        """Returns a string representation of this pipeline."""
        result = 'REGISTER CONTENT\n'
        for i in range(0,len(self.registers),2):
            reg0 = self.registers[i]
            reg1 = self.registers[i+1]
            result += 'R%s: 0x%08x R%s: 0x%08x\n' % (i, reg0, i+1, reg1)
        result += '\nMEMORY CONTENT\n'
        i = 1
        mem_addresses = sorted(self.memory.keys())
        for addr in mem_addresses[:32]:
            packed = struct.pack('@I',self.memory[addr])
            h = binascii.hexlify(packed)
            if i == 1:
                result += '0x%08x %s %s %s %s ' % (addr,h[:2],h[2:4],h[4:6],h[6:])
                i += 1
            elif i == 4:
                result += '%s %s %s %s\n' % (h[:2],h[2:4],h[4:6],h[6:])
                i = 1
            else:
                result += '%s %s %s %s ' % (h[:2],h[2:4],h[4:6],h[6:])
                i += 1
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
            try:
                # fetch the next instruction according current PC
                instr = self.find_instr(self.pc)
                self.do_stages(instr)
            except IndexError:
                self.do_stages(Nop)
            # stop fetching after we have hit HLT
            if type(self.pipeline[0]) is HLTInstruction:
                self.pipeline[0] = Nop
                break

        # flushes the pipeline after we see an HLT
        while self.pipeline != empty_pipe:
            self.do_stages(Nop)

    def do_stages(self, instr):
        """ Steps through the five stages of the pipeline. """
        self.write(self.pipeline[4])
        self.access_mem(self.pipeline[3])
        self.execute(self.pipeline[2])
        self.decode(self.pipeline[1])
        self.fetch(instr)
        print '\n'
        self.cycle_count += 1

    def get_forwarded_val(self, reg):
        """ Handles X-X forwarding and M-X forwarding """
        mstage_instr = self.pipeline[3]
        wstage_instr = self.pipeline[4]
        if type(mstage_instr) is RInstruction or type(wstage_instr) is RInstruction:
            if (mstage_instr.c_signals['RegWrite'] and mstage_instr.rd != 0 
                and reg == mstage_instr.rd and mstage_instr.alu_result is not None):
                print '\tX-X forwarding: RD - %s, value - %s' % (reg, mstage_instr.alu_result)
                return mstage_instr.alu_result 
            # using elif below avoids double data hazards
            elif (wstage_instr.c_signals['RegWrite'] and wstage_instr.rd != 0 
                and reg == wstage_instr.rd and wstage_instr.alu_result is not None):
                print '\tM-X forwarding: RD - %s, value - %s' % (reg, wstage_instr.alu_result)
                return wstage_instr.alu_result 
        elif type(mstage_instr) is IInstruction or type(wstage_instr) is IInstruction:
            if (mstage_instr.c_signals['RegWrite'] and mstage_instr.rt != 0 
                and reg == mstage_instr.rt and mstage_instr.alu_result is not None):
                print '\tX-X forwarding: RT - %s, value - %s' % (reg, mstage_instr.alu_result)
                return mstage_instr.alu_result 
            # using elif below avoids double data hazards
            elif (wstage_instr.c_signals['RegWrite'] and wstage_instr.rt != 0 
                and reg == wstage_instr.rt and wstage_instr.alu_result is not None):
                print '\tM-X forwarding: RT - %s, value - %s' % (reg, wstage_instr.alu_result)
                return wstage_instr.alu_result 
        else:
            return None

    def fetch(self, instr):
        """Fetches the given instruction."""
        s = 'On deck: '
        if self.use_instr:
            s += 'was: %s, now: %s (load use)' % (self.pipeline[0],self.use_instr)
        elif self.stall:
            s += 'was: %s, now: %s (jump stall)' % (self.pipeline[0],Nop)
        else:
            s += '%s' % self.pipeline[0]
        print s + '; hazards: %s' %  self.hazards

        # move the pipeline along!
        if (len(self.pipeline) >= 5):
            self.pipeline.pop()

        # another stage may be asking for a stall, so do Nop instead
        replaced = False
        if self.stall:
            # need to back up the pc when branching so that we don't skip instrs
            if self.branched:
                self.pc -= 4
                self.branched = False
            # fetch this instr at this pc instead of the originally fetched
            instr = self.find_instr(self.pc)
            # replace what was already fetched into the pipeline
            self.pipeline[0] = Nop
            self.pc += 4
            self.stall = False
            replaced = True
        elif self.use_instr:
            # for load-use stalling
            instr = self.pipeline[0] 
            self.pipeline[0] = self.use_instr
            self.use_instr = None
            replaced = True
        else:
            self.pc += 4

        print 'Fetching: %s' % instr
        self.pipeline.appendleft(instr)

        # if we stalled at some point, we have to forget we saw an instr the first time
        if instr is not Nop and not replaced and type(instr) is not HLTInstruction:
            self.instr_count += 1

    def decode(self, instr):
        """Decodes the current instruction."""
        print 'Decoding: %s; hazards: %s' % (instr,self.hazards)
        if instr is not Nop:
            # we need to calculate addresses for j and beq instrs here
            if instr.instr == 'j':
                self.pc = instr.target
                self.stall = True
            elif instr.instr == 'beq':
                val1 = self.registers[instr.rs]
                val2 = self.registers[instr.rt]
                if val1 == val2:
                    self.pc += 4*instr.imm
                    self.stall = True
                    self.branched = True
                    print '\tbranch condition = true, jump to addr %s' % self.pc
                else:
                    print '\tbranch condition = false, move on!'

            # load-use hazard detection
            prev_instr = self.pipeline[2]
            if (prev_instr is not Nop and prev_instr.c_signals['MemRead']
                and (prev_instr.rt == instr.rs or prev_instr.rt == instr.rt)):
                print '\tLoad-use hazard detected! Inserting bubble.'
                self.pipeline[1] = Nop
                self.use_instr = instr

    def execute(self, instr):
        print 'Executing: %s; hazards: %s' % (instr, self.hazards)
        if instr is not Nop and type(instr) is not HLTInstruction:
            i = instr.instr
            c_sigs = instr.c_signals

            if i != 'j' and i != 'beq':
                val1 = self.registers[instr.rs]
                val2 = self.registers[instr.rt] if not c_sigs['ALUSrc'] else instr.imm

                # hazard detection and forwarding for RS reg
                if instr.rs in self.hazards:
                    print '\tHazardous RS found!'
                    forwarded_rs_val = self.get_forwarded_val(instr.rs)
                    if forwarded_rs_val is not None:
                        print '\tForwarded RS val: %s' % forwarded_rs_val
                        val1 = forwarded_rs_val

                # hazard detection and forwarding for RT reg
                if instr.rt in self.hazards:
                    print '\tHazardous RT found!'
                    forwarded_rt_val = self.get_forwarded_val(instr.rt)
                    if forwarded_rt_val is not None:
                        print '\tForwarded RT val: %s' % forwarded_rt_val
                        val2 = forwarded_rt_val if not c_sigs['ALUSrc'] else val2

                instr.alu_result = eval('%s+%s' % (val1,val2))

            # if we're writing to a register as a result of this instruction,
            # we need to add the destination register in as a potential hazard
            if c_sigs['RegWrite']:
                dest = instr.rd if c_sigs['RegDst'] else instr.rt
                self.hazards.append(dest)

    def access_mem(self, instr):
        """Accesses memory to handle LW and SW instructions."""
        print 'Access memory with: %s; hazards: %s' % (instr, self.hazards)
        # sw : M[R[rs]+SignExtImm] = R[rt]
        # lw : R[rt] = M[R[rs]+SignExtImm]
        if instr is not Nop and instr.instr == 'sw':
            self.memory[instr.alu_result] = self.registers[instr.rt]
        elif instr is not Nop and instr.instr == 'lw':
            offset = instr.alu_result
            instr.alu_result = self.memory[offset]

    def write(self, instr):
        """Writes data back to register file."""
        print 'Writing back with: %s; hazards: %s' % (instr, self.hazards)
        if instr is not Nop and instr.c_signals['RegWrite'] and instr.alu_result is not None:
            dest = instr.rd if instr.c_signals['RegDst'] else instr.rt
            self.registers[dest] = instr.alu_result
            if dest in self.hazards:
                self.hazards.remove(dest)
