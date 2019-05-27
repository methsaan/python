#! /usr/bin/python3

import turtle
import math
import time
t = turtle.Pen()
t.speed(1)
t.color("blue")
t.width(5)
a = int(input("Enter length of side a: "))
t.forward(a)
t.left(90)
c = int(input("Enter length of side b: "))
t.forward(c)

a = math.acos((90*90 + c*c - a*a)/2*90*c)
c = math.acos((90*90 + a*a - c*c)/2*90*a)

print(a)
print(c)
print(a+c)
t.forward(math.sqrt(side1**2 + side2**2))
time.sleep(5)
