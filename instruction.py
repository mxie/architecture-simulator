#!/usr/bin/python

# Melissa Xie, Courtney Sims
# EECE 3230 Final Project
# Prof. Fei, April 2012

# maps available opcodes to their instruction
instr_dict = {'000000':'add',
              '001000':'addi',
              '000100':'beq',
              '100011':'lw',
              '101011':'sw',
              '000010':'j',
              '111111':'hlt'}

def bin_to_int(s):
    """Converts a binary string into an integer representation"""
    return int(s, 2)

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
        self.alu_result = None

    def __str__(self):
        """Returns a string representation of this Instruction."""
        return 'addr: %s , opcode: %s'% (self.addr,self.opcode)



class RInstruction(Instruction):
    """Represents an R-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this RInstruction."""
        super(RInstruction,self).__init__(addr,opcode,rem)
        self.rs = bin_to_int(rem[:5])
        self.rt = bin_to_int(rem[5:10])
        self.rd = bin_to_int(rem[10:15])
        self.shamt = bin_to_int(rem[15:20])
        self.funct = bin_to_int(rem[20:])
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
        return '%s %s, %s, %s' % (self.instr, self.rd, self.rs, self.rt)



class IInstruction(Instruction):
    """Represents an I-type MIPS instruction."""

    def __init__(self,addr,opcode,rem):
        """Initializes this IInstruction."""
        super(IInstruction,self).__init__(addr,opcode,rem)
        self.rs = bin_to_int(rem[:5])
        self.rt = bin_to_int(rem[5:10])
        self.imm = bin_to_int(rem[10:]) # do we need to worry about sign extension?
        self.c_signals = self.set_control_signals(self.instr)

    def __str__(self):
        """Returns a string representation of this IInstruction."""
        return '%s %s, %s, %s' % (self.instr, self.rt, self.rs, self.imm)


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
            for s in ['ALUSrc','MemWrite']:
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
        self.target = bin_to_int(rem)*4
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
        return '%s %s' % (self.instr, self.target)



class HLTInstruction(Instruction):
    """Represents a HLT."""

    def __init__(self,addr,opcode,rem):
        """Initializes this HLT."""
        super(HLTInstruction,self).__init__(addr,opcode,rem)

    def __str__(self):
        """Returns a string representation of this HLTInstruction."""
        return 'addr: %s , opcode: %s , rem: %s' % (self.addr, self.opcode, self.rem)
