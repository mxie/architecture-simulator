#!/usr/bin/python

# Melissa Xie, Courtney Sims
# EECE 3230 Final Project

# maps available opcodes to their instruction
instr_dict = {'000000':'add',
              '001000':'addi',
              '000100':'beq',
              '100011':'lw',
              '101011':'sw',
              '000010':'j',
              '111111':'hlt'}


class Nop(object):
    pass


class Instruction(object):
    """Represents a MIPS instruction."""
    global instr_dict

    def __init__(self,addr,opcode,rem):
        """Initializes this Instruction."""
        self.addr = addr
        self.opcode = opcode
        self.rem = rem
        self.instr = instr_dict[opcode]
        self.result = None
        self.unwritten = []

    def __str__(self):
        """Returns a string representation of this Instruction."""
        return 'addr: %s , opcode: %s'% (self.addr,self.opcode)



class RInstruction(Instruction):
    """Represents an R-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this RInstruction."""
        super(RInstruction,self).__init__(addr,opcode,rem)
        self.rs = rem[:5] 
        self.rt = rem[5:10]
        self.rd = rem[10:15]
        self.shamt = rem[15:20]
        self.funct = rem[20:]
        self.c_signals = { 'RegDst': 1,
                           'ALUSrc': 0,
                           'MemtoReg': 0,
                           'RegWrite': 1,
                           'MemRead': 0,
                           'MemWrite': 0,
                           'Branch': 0,
                           'ALUOp1': 1,
                           'ALUOp0': 0,
                           'Jump': 0 }

    def __str__(self):
        """Returns a string representation of this RInstruction."""
        return 'addr: %s , opcode: %s , rs: %s , rt: %s , rd: %s , shamt: %s , funct: %s' % (self.addr, self.opcode, self.rs, self.rt, self.rd, self.shamt, self.funct)
        


class IInstruction(Instruction):
    """Represents an I-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this IInstruction."""
        super(IInstruction,self).__init__(addr,opcode,rem)
        self.rs = rem[:5] 
        self.rt = rem[5:10]
        self.rd = rem[10:15]
        self.imm = rem[15:]
        self.c_signals = self.set_control_signals(self.instr)

    def __str__(self):
        """Returns a string representation of this IInstruction."""
        return 'addr: %s , opcode: %s , rs: %s , rt: %s , imm: %s' % (self.addr, self.opcode, self.rs, self.rt, self.imm)


    def set_control_signals(self,instr):
        signals = { 'RegDst': 0,
                    'ALUSrc': 0,
                    'MemtoReg': 0,
                    'RegWrite': 0,
                    'MemRead': 0,
                    'MemWrite': 0,
                    'Branch': 0,
                    'ALUOp1': 0,
                    'ALUOp0': 0,
                    'Jump': 0 }

        if instr == 'lw':
            for s in ['ALUSrc','MemtoReg','RegWrite','MemRead']:
                signals[s] = 1
        elif instr == 'sw':
            for s in ['MemtoReg','MemWrite']:
                signals[s] = 1
        elif instr == 'addi':
            for s in ['ALUSrc','RegWrite']:
                signals[s] = 1
        elif instr == 'beq':
            for s in ['Branch','ALUOp0']:
                signals[s] = 1

        return signals


class JInstruction(Instruction):
    """Represents a J-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this JInstruction."""
        super(JInstruction,self).__init__(addr,opcode,rem)
        self.target = rem 
        self.c_signals = { 'RegDst': 0,
                           'ALUSrc': 0,
                           'MemtoReg': 0,
                           'RegWrite': 0,
                           'MemRead': 0,
                           'MemWrite': 0,
                           'Branch': 0,
                           'ALUOp1': 0,
                           'ALUOp0': 0,
                           'Jump': 1 }

    def __str__(self):
        """Returns a string representation of this JInstruction."""
        return 'addr: %s , opcode: %s , target: %s' % (self.addr, self.opcode, self.target)
        


class HLTInstruction(Instruction):
    """Represents a HLT."""

    def __init__(self,addr,opcode,rem):
        """Initializes this HLT."""
        super(HLTInstruction,self).__init__(addr,opcode,rem)

    def __str__(self):
        """Returns a string representation of this HLTInstruction."""
        return 'addr: %s , opcode: %s , rem: %s' % (self.addr, self.opcode, self.rem)
