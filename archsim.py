#!/usr/bin/python

# Melissa Xie, Courtney Sims
# EECE 3230 Final Project

import sys
from instr_models import RInstruction, IInstruction, JInstruction, HLTInstruction
from parser import BinaryParser
from pipeline import PipelineSim

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: ./%s binfile' % sys.argv[0]
    else:
        # parse the binary file
        filename = sys.argv[1]
        p = BinaryParser(filename)
        p.parse()

        p_sim = PipelineSim(p.memory,p.instr_list)
        p_sim.advance() 
        print str(p_sim)
