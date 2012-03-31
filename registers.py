#!/usr/bin/python

class Registers(object):
    def __init__(self):
        self.reg = [0 for i in range(32)]

    def to_str(self):
        print self.reg

