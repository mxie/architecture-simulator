#!/usr/bin/python
import sys, binascii
from instr_models import RInstruction, IInstruction, JInstruction

instr_dict = {0b101011:('sw',IInstruction),
              0b100011:('lw',IInstruction),
              0b000000:('add',RInstruction),
              0b001000:('addi',IInstruction),
              0b000100:('beq',IInstruction),
              0b000010:('j',JInstruction),
              0b111111:('hlt')}

output = ''

class BinaryParser(object):
    num_bytes = 16

    def __init__(self,f):
        self.f = f

    def parse(self):
        global output
        instr_list = []
        with open(self.f,'rb') as contents:
            words = contents.read(self.num_bytes)
            starred = False
            addr_counter = 0
            while words:
                hexwords = binascii.hexlify(words)
                if hexwords != '0' * (self.num_bytes * 2):
                    output += self.prettify(hexwords,addr_counter)
                    output += '\n'
                    starred = False
                    instr_list += self.split_instrs(addr_counter,words)
                else:
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
        # how to work at the bit level?!

    def get_bit(slf,byteval,idx):
        return (byteval&(1<<idx))

    def split_instrs(self,addr,words):
        i_list = []
        for i in range(0,len(words),8):
            i_list.append(self.create_instr(addr,words[i:i+8]))
        return i_list

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Usage: %s binfile hexdumpfile' % sys.argv[0]
    else:
        filename = sys.argv[1]
        parser = BinaryParser(filename)
        parser.parse()
        out_file = open(sys.argv[2], "w")
        out_file.seek(0)
        for line in output:
            out_file.write(line)
        out_file.close()
        print '%s successful' % sys.argv[2]
        print output