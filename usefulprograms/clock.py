#! /usr/bin/python3

import time
import datetime
from math import *
from random import *
import subprocess as sp
from sys import *

def print_char(x, y, char):
    print("\033["+str(y)+";"+str(x)+"H"+char)

def print_line(x1, y1, x2, y2, c):
    if y2-y1 != 0:
        xInc = 1 if (y2-y1) < (x2-x1) else ((x2-x1)/(y2-y1) if (y2-y1) != 0 else 1)
        yInc = 1 if (x2-x1) < (y2-y1) else ((y2-y1)/(x2-x1) if (x2-x1) != 0 else 1)
    else:
        xInc = 1
        yInc = 0
    coords = []
    numOfCoords = x2-x1 if (xInc == 1 or y2-y1 == 0) else y2-y1
    for x in range(abs(numOfCoords)):
        temp = -x if numOfCoords < 0 else x
        print_char(x1+int(temp*xInc), y1+int(temp*yInc), c)

print_line(20, 10, 30, 20, "\\")
