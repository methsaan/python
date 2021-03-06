#! /usr/bin/python3

from time import *
import datetime
from math import *
from random import *
import subprocess as sp
from sys import *

def print_char(x, y, char):
    print("\033["+str(y)+";"+str(x)+"H"+char)

def printline(x1, y1, x2, y2):
    xdif = max(x1, x2)-min(x1, x2)
    ydif = max(y1, y2)-min(y1, y2)
    yInc = ydif/xdif if xdif != 0 else 0
    xInc = xdif/ydif if ydif != 0 else 0
    xCoord = min(x1, x2) if x2 > x1 else max(x1, x2)-8
    yCoord = min(y1, y2) if y2 > y1 else max(y1, y2)-1
    for x in range(xdif):
        print_char(int(xCoord), int(yCoord), "#")
        if x2 > x1:
            xCoord += xInc
        else:
            xCoord -= xInc
        if y2 > y1:
            yCoord += yInc
        else:
            yCoord -= yInc

sp.call("clear", shell=True)
xList = [150, 160, 170, 180, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
yList = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50]
for x in range(len(xList)):
    printline(185, 185, xList[x], yList[x])
    sleep(0.01)
    sp.call("clear", shell=True)
