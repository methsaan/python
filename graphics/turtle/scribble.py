#! /usr/bin/python3

import random
import turtle

t = turtle.Pen()

x = 0
t.speed(0)
colors = ["red", "blue2", "cyan", "springgreen", "brown", "orangered", "black", "purple", "deeppink", "greenyellow"]
while True:
    t.color(random.choice(colors))
    t.width(random.randrange(1, 10))
    t.forward(random.randrange(1, 65))
    t.left(random.randrange(0, 293857))
    x = x + 1
    if x == 200:
        quit()
