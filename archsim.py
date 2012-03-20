#!/usr/bin/python
import sys, binascii, struct
from instr_models import RInstruction, IInstruction, JInstruction

# maps available opcodes to their instruction and instruction types
instr_dict = {
              '000000':('add',RInstruction),
              '001000':('addi',IInstruction),
              '000100':('beq',IInstruction),
              '100011':('lw',IInstruction),
              '101011':('sw',IInstruction),
              '000010':('j',JInstruction),
              '111111':('hlt',None)}

output = ''
instr_list = []

class BinaryParser(object):
    num_bytes = 16

    def __init__(self,f):
        self.f = f

    def parse(self):
        global output, instr_list

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
                    output += self.prettify(hexwords,addr_counter)
                    output += '\n'
                    starred = False
                    instr_list += self.split_instrs(addr_counter,words)
                else:
                    # just print 1 line of 0s, but a * to indicate more
                    if not starred:
                        output += self.prettify(hexwords,addr_counter)
                        output += '\n'
                        output += '*\n'
                        starred = True
                words = contents.read(self.num_bytes)
                addr_counter += self.num_bytes
            output += '%08x' % addr_counter

    def prettify(self,s,c):
        byte_addr = '%08x' % c
        result = [s[i:i+2] for i in range(0,len(s),2)]
        return byte_addr + '  ' +  ' '.join(result)

    def create_instr(self,addr,instr):
        global instr_dict

        # read in the string/data in little endian, unsigned format
        unpacked = struct.unpack('<I',instr)[0]
        # get binary representation
        binary = bin(unpacked)[2:]
        binary_instr = self.make_32bit(binary)
        opcode = binary_instr[:6]
        remaining = binary_instr[6:]

        if instr_dict[opcode]:
            instr_type = instr_dict[opcode][1]
            if instr_type == RInstruction:
                return RInstruction(addr,opcode,remaining)
            elif instr_type == IInstruction:
                return IInstruction(addr,opcode,remaining)
            elif instr_type == JInstruction:
                return JInstruction(addr,opcode,remaining)
        else:
            print 'Opcode %s is not a valid instruction' % opcode

    def make_32bit(self, bin):
        if len(bin) < 32:
            pad_num = 32 - len(bin)
            padding = '0' * pad_num
            bin = padding + bin
        return bin

    def split_instrs(self,addr,words):
        i_list = []
        # separating the 16 bytes into 4 instructions
        for i in range(0,len(words),4):
            i_list.append(self.create_instr(addr,words[i:i+4]))
        return i_list

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Usage: ./%s binfile hexdumpfile' % sys.argv[0]
    else:
        # parse the binary file
        filename = sys.argv[1]
        parser = BinaryParser(filename)
        parser.parse()

        # write out hexdump to file
        out_file = open(sys.argv[2], "w")
        for line in output:
            out_file.write(line)
        out_file.close()
        print '%s has been written' % sys.argv[2]
#        print output
