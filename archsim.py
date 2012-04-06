#!/usr/bin/python

# Melissa Xie, Courtney Sims
# EECE 3230 Final Project

import sys
from instr_models import RInstruction, IInstruction, JInstruction, HLTInstruction
from parser import BinaryParser
from pipeline import PipelineSim

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Usage: ./%s binfile hexdumpfile' % sys.argv[0]
    else:
        # parse the binary file
        filename = sys.argv[1]
        p = BinaryParser(filename)
        p.parse()

        p_sim = PipelineSim(p.memory,p.instr_list)
        print str(p_sim)

        # write out hexdump to file
#        out_file = open(sys.argv[2], "w")
#        for line in parser.output:
#            out_file.write(line)
#        out_file.close()
#        print '%s has been written' % sys.argv[2]
#        print output
#        for x in parser.instr_list:
#            print x.to_str()
