#!/usr/bin/python

class PipelineSim(object):
    def __init__(self, instrs):
        self.instr_count = 0
        self.cycle_count = 0
        self.cpi = 0
        self.registers = [0 for i in range(32)]
        self.memory = dict((i*4,0) for i in range(0x00000ffc))
        self.pc = 0x00001000
        self.instructions = instrs

