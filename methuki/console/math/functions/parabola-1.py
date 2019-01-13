#! /usr/bin/python3

import subprocess as sp
import sys
from termcolor import colored, cprint

def print_char(x, y, char, color):
    cprint("\033["+str(y)+";"+str(x)+"H"+char, color)

for x in range(-4,4):
#	sp.call("clear",shell=True)
	y = x*x + 3
	print(x,y)
#	print_char(x, y, "X", "red")
