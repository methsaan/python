#! /usr/bin/python3

import turtle
import time
import random
t = turtle.Pen()

t.speed(0)
t.width(75)
colors = ['red2', 'blue2', 'springgreen', 'yellow2', 'aqua', 'orange', 'hotpink']
t.color(random.choice(colors))
for x in range(3):
    for x in range(150):
        t.color(random.choice(colors))
        t.forward(1)
    t.left(90)
t.right(180)
for x in range(2):
    for x in range(150):
        t.color(random.choice(colors))
        t.forward(1)
    t.right(90)
t.width(2)
t.begin_fill()
t.circle(40)
t.end_fill()
t.setheading(0)
t.up()
t.forward(40)
t.width(25)
t.down()
t.forward(100)
time.sleep(5)
