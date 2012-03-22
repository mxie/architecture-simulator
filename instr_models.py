#!/usr/bin/python

# Melissa Xie, Courtney Sims
# EECE 3230 Final Project

class Instruction(object):
    """Represents a MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this Instruction."""
        self.addr = addr
        self.opcode = opcode
        self.rem = rem

    def to_str(self):
        """Returns a string representation of this Instruction."""
        return 'addr: %s , opcode: %s'% (self.addr,self.opcode)



class RInstruction(Instruction):
    """Represents an R-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this RInstruction."""
        self.rs = rem[:5] 
        self.rt = rem[5:10]
        self.rd = rem[10:15]
        self.shamt = rem[15:20]
        self.funct = rem[20:]
        super(RInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        """Returns a string representation of this RInstruction."""
        return 'addr: %s , opcode: %s , rs: %s , rt: %s , rd: %s , shamt: %s , funct: %s' % (self.addr, self.opcode, self.rs, self.rt, self.rd, self.shamt, self.funct)
        


class IInstruction(Instruction):
    """Represents an I-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this IInstruction."""
        self.rs = rem[:5] 
        self.rt = rem[5:10]
        self.rd = rem[10:15]
        self.imm = rem[15:]
        super(IInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        """Returns a string representation of this IInstruction."""
        return 'addr: %s , opcode: %s , rs: %s , rt: %s , imm: %s' % (self.addr, self.opcode, self.rs, self.rt, self.imm)



class JInstruction(Instruction):
    """Represents a J-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this JInstruction."""
        self.target = rem 
        super(JInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        """Returns a string representation of this JInstruction."""
        return 'addr: %s , opcode: %s , target: %s' % (self.addr, self.opcode, self.target)
        


class HLTInstruction(Instruction):
    """Represents a HLT."""

    def __init__(self,addr,opcode,rem):
        """Initializes this HLT."""
        super(HLTInstruction,self).__init__(addr,opcode,rem)

    def to_str(self):
        """Returns a string representation of this HLTInstruction."""
        return 'addr: %s , opcode: %s , rem: %s' % (self.addr, self.opcode, self.rem)