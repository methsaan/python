#! /usr/bin/python3

import time
import turtle
t = turtle.Pen()

t.speed(0)
left = 50
up = 5
for x in range(5):
    t.forward(left)
    t.left(90)
    t.forward(up)
    t.right(90)
    left = left - 5
    up = up + 5
t.left(90)
left = 0
for x in range(5):
    t.forward(left)
    t.left(90)
    t.forward(up)
    t.right(90)
    left = left - 5
    up = up - 5
time.sleep(3)
