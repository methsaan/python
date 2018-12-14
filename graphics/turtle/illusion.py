#! /usr/bin/python3

import turtle
import time
import random
t = turtle.Pen()

t.speed(0)
t.width(55)
colors = ['springgreen', 'deeppink', 'blue2', 'cyan', 'red', 'yellow', 'orange', 'peachpuff', 'green2']
t.up()
t.goto(-360, 360)
t.down()
t.right(90)
for x in range(10):
    for x in range(240):
        t.forward(3)
        t.color(random.choice(colors))
    t.left(90)
    for x in range(18):
        t.forward(3)
        t.color(random.choice(colors))
    t.left(90)
    for x in range(240):
        t.forward(3)
        t.color(random.choice(colors))
    t.right(90)
    for x in range(18):
        t.forward(3)
        t.color(random.choice(colors))
    t.right(90)
time.sleep(5)
