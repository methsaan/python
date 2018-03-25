#! /usr/bin/python3

import turtle
import time
import random
t = turtle.Pen()

t.speed(0)
t.color("aqua")
for x in range(360):
    for x in range(7):
        t.forward(150)
        t.left(51.4)
        colors = ['red2', 'blue2', 'green2', 'yellow2', 'darkgoldenrod4']
        t.color(random.choice(colors))
    t.right(1)
time.sleep(5)
