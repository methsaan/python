#! /usr/bin/python3

import turtle
import time
import random
t = turtle.Pen()

t.width(55)
colors = ['springgreen', 'deeppink', 'blue2', 'cyan']
t.up()
t.goto(-360, 360)
t.down()
t.right(90)
for x in range(10):
    for x in range(720):
        t.forward(1)
        t.color(random.choice(colors))
    t.left(90)
    for x in range(55):
        t.forward(1)
        t.color(random.choice(colors))
    t.left(90)
    for x in range(720):
        t.forward(1)
        t.color(random.choice(colors))
    t.right(90)
    for x in range(55):
        t.forward(1)
        t.color(random.choice(colors))
    t.right(90)
time.sleep(5)
