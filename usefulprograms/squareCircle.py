#! /usr/bin/python3

import time
import turtle
import math
t = turtle.Pen()

carea = float(input("Enter area of circle: "))
sidelength = math.sqrt(carea)
radius = math.sqrt(carea/math.pi)
t.circle(radius)
t.up()
t.forward(sidelength/2)
t.left(90)
t.forward(radius-sidelength/2)
t.down()
for x in range(4):
    t.forward(sidelength)
    t.left(90)
time.sleep(5)
