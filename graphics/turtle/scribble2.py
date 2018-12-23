#! /usr/bin/python3

import random
import turtle

t = turtle.Pen()

x = 0
t.speed(0)
t.width(3)
while True:
    t.color(random.choice(["red", "orange", "green", "blue", "black", "yellow", "gray", "peachpuff", "pink"]))
    t.circle(random.choice([random.randrange(-65, -20), random.randrange(20, 65)]), random.randrange(120, 240))
    t.left(random.randrange(100000))
    x = x + 1
    if x%50 == 0:
        t.up()
        t.goto(random.randrange(-400, 400), random.randrange(-400, 400))
        t.down()
    if x == 100000:
        quit()
