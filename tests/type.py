#! /usr/bin/python3

class myClass:
    def __init__(self):
        self.a = 100
    def printa(self):
        print(self.a)
mco = myClass()
varlist = [12, 13.24, "hello", True, [12, 14, 25], {"a" : 1, "b" : 2}, (12, 42, 25), None, type(12), mco]


for x in varlist:
    print(str(type(x)))
