#! /usr/bin/python3

import random
point = 0
for x in range(2):
	a = str(random.randrange(100, 999)/100)
	b = str(random.randrange(100, 999)/100)
	x = float(input("What is " + a + " + " + b + "? "))
	if float(a) + float(b) == x:
		point = point + 1
for x in range(2):
	a = str(random.randrange(100, 999)/100)
	b = str(random.randrange(100, 999)/100)
	x = float(input("What is " + a + " x " + b + "? "))
	if float(a) * float(b) == x:
		point = point + 1
for x in range(2):
	a = str(random.randrange(100, 990)/100)
	b = str(random.randrange(100, 990)/100)
	x = float(input("What is " + a + " - " + b + "? "))
	if float(a) - float(b) == x:
		point = point + 1
print("Score: " + str(point))
