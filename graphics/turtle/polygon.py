#! /usr/bin/python3

import turtle
t = turtle.Pen()

x = int(input("How many sides: "))

degs = 360/x

for a in range(x):
    t.forward(x/2+10)
    t.left(degs)
