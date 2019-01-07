#! /usr/bin/python3

import turtle
import math
import time
t = turtle.Pen()
t.speed(1)
t.color("lightblue")
t.width(20)
t.forward(int(input("Enter length of side a: ")))
t.left(90)
t.forward(int(input("Enter length of side b: ")))
t.goto(0, 0)
time.sleep(5)
