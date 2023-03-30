#! /usr/bin/python3

import math
import time
from tkinter import *
from itertools import chain

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()

# Rotate point across another point clockwise by a certain angle (0 degrees = horizontal line to the left)

def rotatePoint(x, y, rotatex, rotatey, angle): # x of point to rotate, y of point to rotate, x of center of rotation, y of center of rotation, angle
    lengthFromRotPoint = math.sqrt(abs(x-rotatex)**2 + abs(y-rotatey)**2) # length from rotation point to rotated point
    if lengthFromRotPoint == 0: # Return original coordinates if center of rotation is equal to given point
        return [x, y]
    angleStart = math.asin(abs(y-rotatey) / lengthFromRotPoint) * (180 / math.pi) # angle from the line made from the two points to the nearest of x-axis
    # Find clockwise angle from left of x-axis to the line made from the two points
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
    # Calculate angle between 360 after rotation
    terminatingAngle = (angleStart + angle) % 360
    angleEnd = None
    # Find angle from the previously-found angle to the nearest x-axis
    if terminatingAngle >= 90 and terminatingAngle < 180:
        angleEnd = 180-terminatingAngle
    elif terminatingAngle >= 180 and terminatingAngle < 270:
        angleEnd = terminatingAngle-180
    elif terminatingAngle >= 270 and terminatingAngle < 360:
        angleEnd = 360-terminatingAngle
    else:
        angleEnd = terminatingAngle
    # Find relative x and y distance from the rotation point given the angle
    yFromRotPoint = abs(lengthFromRotPoint * math.sin(math.radians(angleEnd)))
    xFromRotPoint = abs(lengthFromRotPoint * math.cos(math.radians(angleEnd)))
    newCoordx = 0
    newCoordy = 0
    # Find coordinate from origin
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

def rotate(obj, rotatex, rotatey, angle): # rotate a polygon object
    oldCoords = [] # original coordinates
    for x in range(0, len(canvas.coords(obj)), 2):
        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    # rotate original coords point by point given angle
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    # change coordinates of polygon object
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

def makeOval(xRadius, yRadius, centerx, centery, color, outlineColor, outlineWidth, smoothnessFactor): # draw oval using tkinter polygon given 2 radii and a center
    circumference = 2*math.pi * math.sqrt((xRadius**2 + yRadius**2) / 2)
    angleInterval = 360/circumference
    points = []
    print(circumference)
    for i in range(math.floor(circumference/smoothnessFactor)):
        angle = angleInterval*i*smoothnessFactor
        x = (xRadius*yRadius)/(math.sqrt(yRadius**2 + xRadius**2*math.tan(math.radians(angle))**2))
        y = (xRadius*yRadius)/(math.sqrt(xRadius**2 + (yRadius**2 / math.tan(math.radians(angle))**2))) if angle != 0 else 0
        xCoord = 0
        yCoord = 0
        if angle >= 0 and angle < 90:
            xCoord = centerx - x
            yCoord = centery - y
        elif angle >= 90 and angle < 180:
            xCoord = centerx + x
            yCoord = centery - y
        elif angle >= 180 and angle < 270:
            xCoord = centerx + x
            yCoord = centery + y
        else:
            xCoord = centerx - x
            yCoord = centery + y
        points.append(xCoord)
        points.append(yCoord)
    return canvas.create_polygon(*points, fill=color, outline=outlineColor)

# Test 1 - triangle:

triangle = canvas.create_polygon(150, 350, 350, 350, 250, 100, fill="red", outline="red")

for x in range(720):
    rotate(triangle, 250, 200, 1)
    tk.update()
    time.sleep(0.005)

# Test 2 - square:

square = canvas.create_polygon(100, 100, 300, 100, 300, 300, 100, 300, fill="blue", outline="blue")

for x in range(720):
    rotate(square, 300, 300, 3)
    tk.update()
    time.sleep(0.01)

# Test 3 - oval: 

oval = makeOval(200, 100, 400, 400, "orange", "green", 12, 5)

for x in range(40):
    rotate(oval, 400, 400, 3)
    tk.update()
    time.sleep(0.01)

canvas.mainloop()
