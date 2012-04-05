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
#        self.pipeline = [ FetchStage(),
#                          DecodeStage(),
#                          ExecuteStage(),
#                          MemoryStage(),
#                          WriteStage() ]

        # to populate memory with the data we're starting with
        for i in instrs:
            self.memory[i.addr] = i

    def __str__(self):
        result = 'REGISTER CONTENT\n'
        for i in range(0,len(self.registers),2):
            reg0 = self.registers[i]
            reg1 = self.registers[i+1]
            result += 'R%s: %s R%s: %s\n' % (i, reg0, i+1, reg1)
        result += 'MEMORY CONTENT\n'
        i = 1
        for addr in self.memory.keys():
            if (i == 1):
                result += '0x%08x ...\n' % (addr)
            elif (i == 4):
                result += '\n'
                i = 1
            else:
                i += 1
        return result

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
    def __init__(self,instr):
        self.instr = instr

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

