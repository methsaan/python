#! /usr/bin/python3

import turtle
import math
import time

t = turtle.Pen()
t.left(180)
t.speed(8)
t.color("blue")
t.width(5)
t.begin_fill()
a = int(input("Enter length of side a: "))*10
t.forward(a)
t.right(90)
b = int(input("Enter length of side b: "))*10
t.forward(b)
A = math.asin(b/(math.sqrt(a**2 + b**2)))*(180/math.pi);
t.right(90+A)
t.forward(math.sqrt(a**2 + b**2))
t.end_fill()
time.sleep(5)
