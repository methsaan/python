#! /usr/bin/python3

from time import *
import datetime
from math import *
from random import *
import subprocess as sp

def print_char(x, y, char):
    print("\033["+str(y)+";"+str(x)+"H"+char)

function = input("Enter function to graph: ")
sp.call("clear", shell=True)
print_char(0, 20, "________________________________________")
for i in range(1, 40):
    print_char(20, i, "|")
for x in range(-20, 20):
    exec(function)
    if y in range(-20, 20):
       print_char(x+20, -y+20, "#")
