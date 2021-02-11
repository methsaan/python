#! /usr/bin/python3

import time
import turtle
t = turtle.Pen()

semimajor = int(input("Enter semi-major axis (longest radius): "))
semiminor = int(input("Enter semi-minor axis (shortest radius): "))

d1 = semimajor*2
d2 = semiminor*2

x = 0
y = 0
cntx = 0
cnty = 0

t.up()
t.backward(semimajor)
t.down()
t.forward(d1)
t.up()
t.right(90)
t.down()
t.circle(d2)
t.left(180)
t.up()
t.forward(semimajor)
t.left(90)
t.down()
t.circle(d2)

time.sleep(3)
