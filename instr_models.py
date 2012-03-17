#!/usr/bin/python

class Instruction(object):
    def __init__(self,addr,opcode):
        self.addr = addr
        self.opcode = opcode

class RInstruction(Instruction):
    def __init__(self,addr,opcode,rs,rt,rd,shamt,funct):
        self.rs = rs 
        self.rt = rt
        self.rd = rd
        self.shamt = shamt 
        self.funct = funct
        super(RInstruction,self).__init__(addr,opcode)
        
class IInstruction(Instruction):
    def __init__(self,addr,opcode,rs,rt,imm):
        self.rs = rs 
        self.rt = rt
        self.imm = imm
        super(IInstruction,self).__init__(addr,opcode)

class JInstruction(Instruction):
    def __init__(self,addr,opcode,target):
        self.target = target 
        super(JInstruction,self).__init__(addr,opcode)
