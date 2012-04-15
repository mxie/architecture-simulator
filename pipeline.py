#!/usr/bin/python
from collections import deque
from instr_models import HLTInstruction, RInstruction, IInstruction, JInstruction, Nop

class PipelineSim(object):
    def __init__(self, memory, instrs):
        self.instr_count = 0
        self.cycle_count = 0
        self.cpi = 0
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

        result += 'MEMORY CONTENT\n'
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
            i = self.instructions.popleft()
            if type(i) is HLTInstruction:
                while self.pipeline is not empty_pipe:
                    self.pipeline.pop()
                    self.pipeline.appendleft(Nop)
                return
            else:
                self.do_stages()
        
    def do_stages():
        self.write(self.pipeline[4])
        self.access_mem(self.pipeline[3])
        self.execute(self.pipeline[2])
        self.decode(self.pipeline[1])
        self.fetch(self.pipeline[0])

    def fetch(self, instr):
        if (len(self.pipeline) >= 5):
            self.pipeline.pop()
        self.pipeline.appendleft(instr)

    def decode(self, instr):
        pass

    def execute(self, instr):
        if type(instr) == Nop:
            pass
        else:
            # a bunch of stuff here

    def access_mem(self, instr):
        if type(instr) == Nop:
            pass
        else:
            # a bunch of stuff here

    def write(self, instr):
        if type(instr) == Nop:
            pass
        else:
            # a bunch of stuff here
