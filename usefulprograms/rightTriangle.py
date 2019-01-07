#! /usr/bin/python3

import turtle
import math
import time
t = turtle.Pen()
t.speed(1)
t.color("lightblue")
t.width(20)
side1 = int(input("Enter length of side a: "))
t.forward(side1)
t.left(90)
side2 = int(input("Enter length of side b: "))
t.forward(side2)
time.sleep(5)
