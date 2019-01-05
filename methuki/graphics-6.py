#! /usr/bin/python3

import random
import time
import turtle
fred = turtle.Pen()
fred.shape("turtle")

fred.speed(0)

def rand(a, b):
	return random.randrange(a, b)
fred.up()
fred.backward(500)
fred.down()
for x in range(1000):
	fred.color("gray"+str(rand(1, 100)))
	fred.width(rand(1, 100))
	fred.forward(10)
time.sleep(5)
