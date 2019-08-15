#! /usr/bin/python3

from time import *
import datetime
from math import *
from random import *
import subprocess as sp

def print_char(x, y, char):
    print("\033["+str(y)+";"+str(x)+"H"+char)

for a in list(range(-10, 10))[::-1]:
    function = "y = x*" + str(int(1.5**a))
    sp.call("clear", shell=True)
    print_char(0, 30, "____________________________________________________________")
    for i in range(1, 60):
        print_char(30, i, "|")
    for x in range(-30, 30):
        exec(function)
        if y in range(-30, 30):
            print_char(x+30, -y+30, "#")
    sleep(0.1)
