#! /usr/bin/python3

import time
import turtle
fred = turtle.Pen()
fred.shape("turtle")

fred.reset()

fred.color("springgreen")
fred.width(12)
fred.circle(160)

fred.up()
fred.left(90)
fred.forward(40)
fred.down()
fred.color("red")
fred.begin_fill()
fred.width(6)
fred.circle(80)
fred.end_fill()
time.sleep(10)
