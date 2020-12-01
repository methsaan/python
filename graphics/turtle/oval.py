#! /usr/bin/python3

import time
import turtle
t = turtle.Pen()

semimajor = int(input("Enter semi-major axis: "))
semiminor = int(input("Enter semi-minor axis: "))

d1 = semimajor*2
d2 = semiminor*2

x = 0
y = 0
cntx = 0
cnty = 0

listmaj = [50, 40, 30, 20, 10]
listmin = [50, 40, 30, 20, 10]

while x < semiminor and y < semimajor:
	t.forward(listmin[x])
	t.left(90)
	t.forward(listmaj[y])
	t.right(90)
	x += 1
	y += 1
	cntx += listmin[x]
	cnty += listmaj[y]

time.sleep(3)
