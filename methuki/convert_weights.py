#! /usr/bin/python3

import subprocess as sp

sp.call("clear",shell=True)

print("This is a program to convert your weight between lbs and kg")

weight_unit = input("Is that lbs or kg (l/k) ?")

if weight_unit != "l" and weight_unit != "k":
	print("ERR: unit has to be l(lbs) or k(kg)")
	quit()

weight = float(input("What is your weight ?"))

if weight_unit == "k":
	your_weight = weight * 2.2
else:
	your_weight = weight / 2.2

print("Your weight in kilo grams is: %.2f %s"%(your_weight,"l" if weight_unit == "k" else "k"))
