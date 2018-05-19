#! /usr/bin/python3

import random
point = 0
for x in range(2):
	a = str(round(random.uniform(10.0, 99.0), 2))
	b = str(round(random.uniform(10.0, 99.0), 2))
	x = float(input("What is " + a + " + " + b + "? "))
	if float(a) + float(b) == x:
		point = point + 1
for x in range(2):
	a = str(round(random.uniform(1.0, 9.0), 2))
	b = str(round(random.uniform(1.0, 9.0), 1))
	x = float(input("What is " + a + " x " + b + "? "))
	if float(a) * float(b) == x:
		point = point + 1
for x in range(2):
	a = str(round(random.uniform(10.0, 99.0), 2))
	b = str(round(random.uniform(10.0, 99.0), 2))
	x = float(input("What is " + a + " - " + b + "? "))
	if float(a) - float(b) == x:
		point = point + 1
print("Score: " + str(point))
