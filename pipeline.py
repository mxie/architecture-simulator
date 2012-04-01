#!/usr/bin/python

class PipelineSim(object):
    def __init__(self, instrs):
        self.instr_count = 0
        self.cycle_count = 0
        self.cpi = 0
        self.registers = [0 for i in range(32)]
        self.memory = dict((i*4,0) for i in range(0x00000ffc/4))
        self.pc = 0x00001000
        self.instructions = instrs

        # to populate memory with the data we're starting with
        for i in instrs:
            self.memory[i.addr] = i

class PipelineStage(object):
    def __init__(self):
        self.register_rs =
        self.register_rt =
        self.register_rd =

class FetchStage(PipelineStage):
    def __init__(self):
        super(FetchStage,self).__init__()

class DecodeStage(PipelineStage):
    def __init__(self):
        super(DecodeStage,self).__init__()

class ExecuteStage(PipelineStage):
    def __init__(self):
        super(ExecuteStage,self).__init__()

class MemoryStage(PipelineStage):
    def __init__(self):
        super(MemoryStage,self).__init__()

class WriteStage(PipelineStage):
    def __init__(self):
        super(WriteStage,self).__init__()

