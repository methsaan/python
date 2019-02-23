#! /usr/bin/python3

import time
product = ""
productbackward = ""

for factor1 in range(65536):
	for factor2 in range(65536):
		productbackward = ""
		product = str(factor1 *factor2)
		for x in range(len(product)):
			productbackward += product[-(x+1)]
		if productbackward == product:
			print(str(factor1) + " \u00D7 " + str(factor2) + " = " + product)
