#! /usr/bin/python3

import time
import turtle
t = turtle.Pen()

size = int(input("Enter size: "))*10

pos = [0, 0]

for x in range(int(size/10)):
    t.goto(pos[0], pos[1])
    pos[0] += size-10*x
    pos[1] += x**2*10

time.sleep(3)
