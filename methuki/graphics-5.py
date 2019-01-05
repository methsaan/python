#! /usr/bin/python3

import time
import turtle
fred = turtle.Pen()
fred.shape("turtle")

fred.speed(0)

fred.color("springgreen")
fred.width(12)
fred.circle(160)

fred.up()
fred.left(90)
fred.forward(80)
fred.right(90)
fred.backward(80)
fred.down()
fred.color("red")
fred.begin_fill()
fred.width(6)
for x in range(4):
	fred.forward(160)
	fred.left(90)
fred.end_fill()
time.sleep(5)
