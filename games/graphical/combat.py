#! /usr/bin/python3

import random
import math
from itertools import chain
import time
from tkinter import *

tk = Tk()
tk.title("Combat")
canvas = Canvas(tk, height=600, width=1080, bg="white", bd=0, highlightbackground="white")
canvas.pack()

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
        newCoordy = rotatey + yFromRotPoint
    elif terminatingAngle >= 270 and terminatingAngle < 360:
        newCoordx = rotatex - xFromRotPoint
        newCoordy = rotatey + yFromRotPoint
    else:
        newCoordx = rotatex - xFromRotPoint
        newCoordy = rotatey - yFromRotPoint
    return [newCoordx, newCoordy]

def reflect(obj, reflectx, reflecty):
    oldCoords = []
    for x in range(0, len(canvas.coords(obj)), 2):
        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    if reflectx != None:
        for x in oldCoords:
            newCoords.append([2 * reflectx - x[0], x[1]])
    if reflecty != None:
        if reflectx != None:
            oldCoords = newCoords
        newCoords = []
        for x in oldCoords:
            newCoords.append([x[0], 2 * reflecty - x[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

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

class character():
    def __init__(self, x, y, maskColor, jointColor, partsColor, extra, forwardDir):
        self.head = makeOval(30, 30, x, y-75, jointColor, "black", 1, 10)
        if extra:
            self.extra = canvas.create_polygon(x+5, y-50, x-25, y-90, x+28, y-90,fill=partsColor, outline="black")
        self.mask = makeOval(21,5,x+7,y-80, maskColor,"black",2,10)
        self.body = canvas.create_polygon(x-30, y-50, x+30, y-50, x+30, y+50, x-30, y+50, fill=partsColor, outline="black")
        self.bicep = makeOval(50,15,x+50,y-20,partsColor,"black",2,10)
        self.forearm = makeOval(30,10,x+100,y-20,partsColor,"black",2,10)
        self.hand = makeOval(15,15,x+130,y-20,jointColor,"black",2,10)
        self.shoulder = makeOval(18,18,x+30,y-20,jointColor,"black",2,10)
        self.arm = [self.bicep, self.forearm, self.hand, self.shoulder] # All arm parts
        for i in self.arm: # Rotate all arm parts 45 degrees clockwise accross center of shoulder
            rotate(i, x+30, y-20, 45)
        self.bicep2 = makeOval(50,15,x,y-20,partsColor,"black",2,10)
        self.forearm2 = makeOval(30,10,x+50,y-20,partsColor,"black",2,10)
        self.hand2 = makeOval(15,15,x+80,y-20,jointColor,"black",2,10)
        self.shoulder2 = makeOval(18,18,x-20,y-20,jointColor,"black",2,10)
        self.arm2 = [self.bicep2, self.forearm2, self.hand2, self.shoulder2] # All arm parts
        for i in self.arm2: # Rotate all arm parts 45 degrees clockwise accross center of shoulder
            rotate(i, x-30, y-20, 110)
        self.leg1 = makeOval(13,40,x+15,y+70,partsColor,"black",10,10)
        self.leg2 = makeOval(13,40,x-18,y+70,partsColor,"black",10,10)
        self.lowerleg = makeOval(10,30,x-20,y+120,partsColor,"black",1,10)
        self.lowerleg2 = makeOval(10,30,x+15,y+120,partsColor,"black",1,10)
        self.knee = makeOval(10,10,x-20,y+95,jointColor,"black",10,10)
        self.knee2 = makeOval(10,10,x+15,y+95,jointColor,"black",10,10)
        self.feet = canvas.create_polygon(x+10, y+145, x+40, y+145, x+40, y+160, x+10, y+160, fill=jointColor, outline="black")
        self.feet2 = canvas.create_polygon(x-25, y+145, x+5, y+145, x+5, y+160, x-25, y+160, fill=jointColor, outline="black")
        self.fullBody = [self.head, self.mask, self.body, *self.arm, *self.arm2, self.leg1, self.leg2, self.lowerleg, self.lowerleg2, self.knee, self.knee2, self.feet, self.feet2]
        if forwardDir == "left":
            for i in self.fullBody:
                reflect(i, x, None)

offensep1 = character(100, 300, "orange", "navy", "silver", False, "right")
offensep2 = character(400, 300, "orange", "gold", "silver", True, "left")

canvas.mainloop()
