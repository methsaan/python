#! /usr/bin/python3

class parent():
    def __init__(self):
       self.a = 28
       self.b = "string1"
       self.c = 3.14
    def printvars(self):
        print(self.a, self.b, self.c)
class child(parent):
    def __init__(self):
        self.a = 25
        self.b = "string2"
        self.c = 3.142857142
        self.d = False
        self.e = None
        self.f = type(self.b)
        self.g = (12, 13, 24, 124)
class child2(parent):
    def __init__(self):
        self.a = 12
        self.b = "string3"
        self.c = 3.141592653
        self.d = True
        self.e = None
        self.f = type(parent)
        self.g = {"a" : self.a, "b" : self.b, "c" : self.c}
p = parent()
c1 = child()
c2 = child2()
objlist = [p, c1, c2]
print(p.a)
print(p.b)
print(p.c)
print(c1.d)
print(c1.e)
print(c1.f)
print(c1.g)
print(c2.a)
print(c2.b)
print(c2.c)
print(c2.d)
print(c2.e)
print(c2.f)
print(c2.g)
p.printvars()
c1.printvars()
c2.printvars()
print()
for x in objlist:
    x.printvars()
