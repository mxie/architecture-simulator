#!/usr/bin/python
from collections import deque
from instr_models import HLTInstruction

class PipelineSim(object):
    def __init__(self, memory, instrs):
        self.instr_count = 0
        self.cycle_count = 0
        self.cpi = 0
        self.registers = [0 for i in range(32)]
        self.memory = memory 
        self.pc = 0x00001000
        self.instructions = deque(instrs)
        self.pipeline = deque([])

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
        while True:
            i = self.instructions.popleft()
            if type(i) is HLTInstruction:
                while self.pipeline:
                    self.pipeline.pop()
                return
            else:
                if (len(self.pipeline) == 5):
                    self.pipeline.pop()
                self.pipeline.appendleft(i)
        
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

