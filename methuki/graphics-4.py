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
fred.down()
fred.color("red")
fred.begin_fill()
fred.width(6)
fred.circle(80)
fred.end_fill()
time.sleep(5)
