#! /usr/bin/python3

import turtle
import time
import random
t = turtle.Pen()

t.speed(0)
t.width(5)
colors = ['green2', 'deeppink', 'blue2', 'cyan', 'red2', 'yellow', 'teal']
t.up()
t.goto(-360, 360)
t.down()
for x in range(900):
    t.color(random.choice(colors))
    t.up()
    t.goto(random.randrange(-360, 320), random.randrange(-360, 320))
    t.down()
    t.begin_fill()
    t.circle(random.randrange(10, 60))
    t.end_fill()
    time.sleep(0.00025)
time.sleep(5)
