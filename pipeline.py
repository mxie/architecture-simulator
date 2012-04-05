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
        self.pipeline = [ FetchStage(),
                          DecodeStage(),
                          ExecuteStage(),
                          MemoryStage(),
                          WriteStage() ]

        # to populate memory with the data we're starting with
        for i in instrs:
            self.memory[i.addr] = i


class PipelineStage(object):
    def __init__(self,instr,sim):
        self.instr = instr
        self.sim = sim

class FetchStage(PipelineStage):
    def __init__(self):
        super(FetchStage,self).__init__(instr,sim)

class DecodeStage(PipelineStage):
    def __init__(self):
        super(DecodeStage,self).__init__(instr,sim)

class ExecuteStage(PipelineStage):
    def __init__(self):
        super(ExecuteStage,self).__init__(instr,sim)

class MemoryStage(PipelineStage):
    def __init__(self):
        super(MemoryStage,self).__init__(instr,sim)

class WriteStage(PipelineStage):
    def __init__(self):
        super(WriteStage,self).__init__(instr,sim)


class PipelineReg(object):
    def __init__(self):

class FDReg(PipelineReg):
    def __init__(self):
        super(FDReg,self).__init__(instr)
        self.register_rs = None
        self.register_rt = None
        self.register_rd = None

class DXReg(PipelineReg):
    def __init__(self):
        super(DXReg,self).__init__(instr)
        self.register_rs = None
        self.register_rt = None
        self.register_rd = None
        self.mem_read = None

class XMReg(PipelineReg):
    def __init__(self):
        super(XMReg,self).__init__(instr)
        self.reg_write = None
        self.register_rd = None

class MWReg(PipelineReg):
    def __init__(self):
        super(MWReg,self).__init__(instr)
        self.reg_write = None
        self.register_rd = None

