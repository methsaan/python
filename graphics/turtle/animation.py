#! /usr/bin/python3

import random
import time
import turtle
t = turtle.Pen()

t.speed(0)
for x in range(60):
    t.clear()
    t.forward(20)
    t.left(6)
    t.color("black")
    t.begin_fill()
    t.circle(70)
    t.end_fill()
