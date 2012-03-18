#!/usr/bin/python

class Instruction(object):
    def __init__(self,addr,opcode,rem):
        self.addr = addr
        self.opcode = opcode
        self.rem = rem

    def to_str(self):
        return 'addr: %s , opcode: %s'% (self.addr,self.opcode)



class RInstruction(Instruction):
    def __init__(self,addr,opcode,rem):
        self.rs = rem[:5] 
        self.rt = rem[5:10]
        self.rd = rem[10:15]
        self.shamt = rem[15:20]
        self.funct = rem[20:]
        super(RInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        return 'addr: %s , opcode: %s , rs: %s , rt: %s , rd: %s , shamt: %s , funct: %s' % (self.addr, self.opcode, self.rs, self.rt, self.rd, self.shamt, self.funct)
        


class IInstruction(Instruction):
    def __init__(self,addr,opcode,rem):
        self.rs = rem[:5] 
        self.rt = rem[5:10]
        self.rd = rem[10:15]
        self.imm = rem[15:]
        super(IInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        return 'addr: %s , opcode: %s , rs: %s , rt: %s , imm: %s' % (self.addr, self.opcode, self.rs, self.rt, self.imm)



class JInstruction(Instruction):
    def __init__(self,addr,opcode,rem):
        self.target = rem 
        super(JInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        return 'addr: %s , opcode: %s , target: %s' % (self.addr, self.opcode, self.target)
