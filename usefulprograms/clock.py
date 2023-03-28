#! /usr/bin/python3

import time
import datetime
import math
import subprocess as sp

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

def rotatePoint(x, y, rotatex, rotatey, angle):
    lengthFromRotPoint = math.sqrt(abs(x-rotatex)**2 + abs(y-rotatey)**2)
    if lengthFromRotPoint == 0:
        return [x, y]
    angleStart = math.asin(abs(y-rotatey) / lengthFromRotPoint) * (180 / math.pi)
    if x < rotatex and y < rotatey:
        pass
    elif x > rotatex and y < rotatey:
        angleStart = 180-angleStart
    elif x > rotatex and y > rotatey:
        angleStart = 180+angleStart
    elif x < rotatex and y > rotatey:
        angleStart = 360-angleStart
    elif x == rotatex and y > rotatey:
        angleStart = 270
    elif x == rotatex and y < rotatey:
        angleStart = 90
    elif x > rotatex and y == rotatey:
        angleStart = 180
    else:
        angleStart = 0
    terminatingAngle = (angleStart + angle) % 360
    angleEnd = None
    if terminatingAngle >= 90 and terminatingAngle < 180:
        angleEnd = 180-terminatingAngle
    elif terminatingAngle >= 180 and terminatingAngle < 270:
        angleEnd = terminatingAngle-180
    elif terminatingAngle >= 270 and terminatingAngle < 360:
        angleEnd = 360-terminatingAngle
    else:
        angleEnd = terminatingAngle
    yFromRotPoint = abs(lengthFromRotPoint * math.sin(math.radians(angleEnd)))
    xFromRotPoint = abs(lengthFromRotPoint * math.cos(math.radians(angleEnd)))
    newCoordx = 0
    newCoordy = 0
    if terminatingAngle >= 90 and terminatingAngle < 180:
        newCoordx = rotatex + xFromRotPoint
        newCoordy = rotatey - yFromRotPoint
    elif terminatingAngle >= 180 and terminatingAngle < 270:
        newCoordx = rotatex + xFromRotPoint
        newCoordy = rotatex + yFromRotPoint
    elif terminatingAngle >= 270 and terminatingAngle < 360:
        newCoordx = rotatex - xFromRotPoint
        newCoordy = rotatey + yFromRotPoint
    else:
        newCoordx = rotatex - xFromRotPoint
        newCoordy = rotatey - yFromRotPoint
    return [newCoordx, newCoordy]

for x in range(360):
    print_line(int(rotatePoint(30, 10, 30, 20, x)[0]), int(rotatePoint(30, 10, 30, 20, x)[1]), 30, 20, "\\")
    sp.call("clear", shell=True)
