#!/usr/bin/python
import binascii, struct
from instruction import RInstruction, IInstruction, JInstruction, HLTInstruction

# maps available opcodes to their instruction and instruction types
instr_dict = {'000000':('add',RInstruction),
              '001000':('addi',IInstruction),
              '000100':('beq',IInstruction),
              '100011':('lw',IInstruction),
              '101011':('sw',IInstruction),
              '000010':('j',JInstruction),
              '111111':('hlt',HLTInstruction)}

class BinaryParser(object):
    """Used to parse binary files into MIPS instructions."""
    num_bytes = 16
    max_data_addr = 0xffc
    max_mem_addr = 0x2000

    def __init__(self,f):
        """Initialize this BinaryParser."""
        self.f = f
        self.output = ''
        self.instr_list = []
        self.memory = dict([ (i,0) for i in range(0,self.max_mem_addr,4) ])

    def parse(self):
        """Reads instructions from a binary file, puts them into data structures, 
        and generates the output which is written to the hexdump file."""

        with open(self.f,'rb') as contents:
            # reads in the file contents 16 bytes at a time
            words = contents.read(self.num_bytes)
            starred = False     # indicate when to use * to represent null lines
            addr_counter = 0    # address counter
            while words:
                # gets hex string rep of binary data
                hexwords = binascii.hexlify(words)
                # if it's NOT just a line of 0s, print them out
                if hexwords != '0' * (self.num_bytes * 2):
                    self.output += self.prettify(hexwords,addr_counter)
                    self.output += '\n'
                    starred = False
                    self.instr_list += self.split_instrs(addr_counter,words)
                else:
                    # just print 1 line of 0s, but a * to indicate more
                    if not starred:
                        self.output += self.prettify(hexwords,addr_counter)
                        self.output += '\n'
                        self.output += '*\n'
                        starred = True
                words = contents.read(self.num_bytes)
                addr_counter += self.num_bytes
            self.output += '%08x' % addr_counter

    def prettify(self,s,c):
        """Given hexwords and the address counter, returns a more readable 
        representation which can be printed to the hexdump."""
        byte_addr = '%08x' % c
        result = [s[i:i+2] for i in range(0,len(s),2)]
        return byte_addr + '  ' +  ' '.join(result)

    def split_instrs(self,addr,words):
        """Splits the given words into 4 instructions and loads data directly into memory."""
        i_list = []
        offset = 0
        for i in range(0,len(words),4):
            actual_addr = addr+offset
            data = words[i:i+4]
            # only create instructions that start at 0x1000
            if actual_addr > self.max_data_addr:
                i_list.append(self.create_instr(actual_addr,data))
            # store all data into memory (both data and instruction segments)
            self.memory[actual_addr] = self.hex_to_int(data)
            offset += 4
        return i_list

    def create_instr(self,addr,instr):
        """Creates an Instruction of the appropriate type based on the given instr."""
        global instr_dict

        binary = self.hex_to_bin(instr)
        opcode = binary[:6]
        remaining = binary[6:]

        if instr_dict[opcode]:
            instr_type = instr_dict[opcode][1]
            if instr_type == RInstruction:
                return RInstruction(addr,opcode,remaining)
            elif instr_type == IInstruction:
                return IInstruction(addr,opcode,remaining)
            elif instr_type == JInstruction:
                return JInstruction(addr,opcode,remaining)
            elif instr_type == HLTInstruction:
                return HLTInstruction(addr,opcode,remaining)
        else:
            print 'Opcode %s is not a valid instruction' % opcode

    def hex_to_int(self,data):
        """ Reads in data string in little endian, unsigned format and returns an int. """
        return struct.unpack('<I',data)[0]

    def hex_to_bin(self,s):
        """Converts a hex data into a 32-bit binary string"""
        int_rep = self.hex_to_int(s)
        binary_str = bin(int_rep)[2:]
        return self.make_32bit(binary_str)
    
    def make_32bit(self, bin):
        """If an instruction is less than 32 bits, pads the front with zeros."""
        if len(bin) < 32:
            pad_num = 32 - len(bin)
            padding = '0' * pad_num
            bin = padding + bin
        return bin

