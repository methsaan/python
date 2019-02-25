#! /usr/bin/python3

import time
import turtle
t = turtle.Pen()

t.speed(0)
t.up()
t.right(90)
t.forward(100)
t.left(90)
t.down()
secs = int(input("How many seconds: "))
for x in range(secs):
    t.color("aqua")
    t.width(100)
    tick = 360 / secs
    time.sleep(.95)
    t.circle(200, tick)
t.color("orangered")
t.begin_fill()
t.circle(200)
t.end_fill()
time.sleep(1)
print("Time's up")
