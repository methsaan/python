#! /usr/bin/python3

import random
import math
from itertools import chain
import time
from tkinter import *

tk = Tk()
tk.title("Combat")

scale = 1

canvas = Canvas(tk, height=850*scale, width=1700*scale, bg="white", bd=0, highlightbackground="white")
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
    def __init__(self, x, y, maskColor, extraColor, headColor, jointColor, partsColor, extra, forwardDir):
        self.x = x
        self.y = y
        self.forwardDir = forwardDir
        self.head = makeOval(12*scale, 12*scale, x*0.5*scale, (y-75)*0.5*scale, headColor, "black", 1, 5*scale)
        if extra:
            self.extra = canvas.create_polygon(x*0.5*scale, (y-55)*0.5*scale, (x-20)*0.5*scale, (y-90)*0.5*scale, (x+20)*0.5*scale, (y-90)*0.5*scale, fill=extraColor, outline="black")
        self.mask = makeOval(10.5*scale, 2.5*scale, (x+7)*0.5*scale, (y-80)*0.5*scale, maskColor, "black", 2, 5*scale)
        self.bicep = makeOval(25*scale, 7.5*scale, (x+50)*0.5*scale, (y-20)*0.5*scale, partsColor, "black", 2, 5*scale)
        self.forearm = makeOval(15*scale, 5*scale, (x+100)*0.5*scale, (y-20)*0.5*scale, partsColor, "black", 2, 5*scale)
        self.hand = makeOval(7.5*scale, 7.5*scale, (x+130)*0.5*scale, (y-20)*0.5*scale, jointColor, "black", 2, 5*scale)
        self.shoulder = makeOval(9*scale, 9*scale, (x+30)*0.5*scale, (y-20)*0.5*scale, jointColor, "black", 2, 5*scale)
        self.arm = [self.bicep, self.forearm, self.hand, self.shoulder] # All arm parts
        for i in self.arm: # Rotate all arm parts 45 degrees clockwise accross center of shoulder
            rotate(i, (x+30)*0.5*scale, (y-20)*0.5*scale, 45)
        self.body = canvas.create_polygon((x-30)*0.5*scale, (y-50)*0.5*scale, (x+30)*0.5*scale, (y-50)*0.5*scale, (x+30)*0.5*scale, (y+50)*0.5*scale, (x-30)*0.5*scale, (y+50)*0.5*scale, fill=partsColor, outline="black")
        self.leg1 = makeOval(6.5*scale, 20*scale, (x+15)*0.5*scale, (y+70)*0.5*scale, partsColor, "black", 10, 5*scale)
        self.lowerleg = makeOval(5*scale, 15*scale, (x+15)*0.5*scale, (y+120)*0.5*scale, partsColor, "black", 1, 5*scale)
        self.knee = makeOval(5*scale, 5*scale, (x+15)*0.5*scale, (y+95)*0.5*scale, jointColor, "black", 10, 5*scale)
        self.feet = canvas.create_polygon((x+10)*0.5*scale, (y+145)*0.5*scale, (x+40)*0.5*scale, (y+145)*0.5*scale, (x+40)*0.5*scale, (y+160)*0.5*scale, (x+10)*0.5*scale, (y+160)*0.5*scale, fill=jointColor, outline="black")
        self.leg2 = makeOval(6.5*scale, 20*scale, (x-18)*0.5*scale, (y+70)*0.5*scale, partsColor, "black", 10, 5*scale)
        self.lowerleg2 = makeOval(5*scale, 15*scale, (x-20)*0.5*scale, (y+120)*0.5*scale, partsColor, "black", 1, 5*scale)
        self.knee2 = makeOval(5*scale, 5*scale, (x-20)*0.5*scale, (y+95)*0.5*scale, jointColor, "black", 10, 5*scale)
        self.feet2 = canvas.create_polygon((x-25)*0.5*scale, (y+145)*0.5*scale, (x+5)*0.5*scale, (y+145)*0.5*scale, (x+5)*0.5*scale, (y+160)*0.5*scale, (x-25)*0.5*scale, (y+160)*0.5*scale, fill=jointColor, outline="black")
        self.bicep2 = makeOval(25*scale, 7.5*scale, x*0.5*scale, (y-20)*0.5*scale, partsColor, "black", 2, 10*scale)
        self.forearm2 = makeOval(15*scale, 5*scale, (x+50)*0.5*scale, (y-20)*0.5*scale, partsColor, "black", 2, 5*scale)
        self.hand2 = makeOval(7.5*scale, 7.5*scale, (x+80)*0.5*scale, (y-20)*0.5*scale, jointColor, "black", 2, 5*scale)
        self.shoulder2 = makeOval(9*scale, 9*scale, (x-20)*0.5*scale, (y-20)*0.5*scale, jointColor, "black", 2, 5*scale)
        self.arm2 = [self.bicep2, self.forearm2, self.hand2, self.shoulder2] # All arm parts
        for i in self.arm2: # Rotate all arm parts 110 degrees clockwise accross center of shoulder
            rotate(i, (x-20)*0.5*scale, (y-20)*0.5*scale, 110)
        self.fullBody = [self.head, self.extra if extra else -1, self.mask, self.body, *self.arm, *self.arm2, self.leg1, self.leg2, self.lowerleg, self.lowerleg2, self.knee, self.knee2, self.feet, self.feet2]
        if forwardDir == "left":
            for i in self.fullBody:
                reflect(i, x*0.5*scale, None)
        self.fullBodyOrigCoords = {}
        for i in self.fullBody:
            self.fullBodyOrigCoords[i] = canvas.coords(i)
        self.rotateFunctions = [self.leftRotate, rotate]
    def leftRotate(self, obj, rotatex, rotatey, angle):
        rotate(obj, 2*(self.x*0.5*scale)-rotatex, rotatey, 360-angle)
    def resetPos(self, x, y):
        for i in self.fullBody:
            origCoords = canvas.coords(i)
            for j in range(0, len(origCoords), 2):
                self.fullBodyOrigCoords[i][j] = self.fullBodyOrigCoords[i][j] + x
                self.fullBodyOrigCoords[i][j+1] = self.fullBodyOrigCoords[i][j+1] + y
            canvas.coords(i, self.fullBodyOrigCoords[i])
    def mvt1(self, direction, distance):
        self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.forearm, rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[0], rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[1], 270)
        self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.hand, rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[0], rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[1], 270)
        for i in self.arm:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 330)
        self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.forearm2, rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[0], rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[1], 270)
        self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.hand2, rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[0], rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[1], 270)
        for i in self.arm2:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 20)

        for i in [self.lowerleg, self.knee, self.feet]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+95)*0.5*scale, 90)

        for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 330)

    def mvt2(self, direction, distance):
        for i in [self.lowerleg2, self.knee2, self.feet2]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y+95)*0.5*scale, 90)

        for i in [self.leg2, self.lowerleg2, self.knee2, self.feet2]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-18)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 300)

        for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 30)

        for i in self.arm:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 180)

        for i in self.arm2:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 280)

    def mvt3(self, direction, distance):
        for i in [self.leg2, self.lowerleg2, self.knee2, self.feet2]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-18)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 120)

        for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 300)

        for i in self.arm:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 180)

        for i in self.arm2:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 160)
        for i in self.fullBody:
            canvas.move(i, 30*scale*0.5 if direction == "forward" else -30*scale*0.5, 0)
        self.x += 30 if direction == "forward" else -30

    def mvt4(self, direction, distance):
        for i in [self.leg2, self.lowerleg2, self.knee2, self.feet2]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-18)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 240)

        for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 60)

        for i in self.arm:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 180)

        for i in self.arm2:
            self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 200)
        for i in self.fullBody:
            canvas.move(i, 30*scale*0.5 if direction == "forward" else -30*scale*0.5, 0)
        self.x += 30 if direction == "forward" else -30

    def mvt5(self, direction, distance):
        self.resetPos(4*30*scale*0.5 if direction == "forward" else 4*-30*scale*0.5, 0)
        self.x += 60 if direction == "forward" else -60

    #def move(self, direction, distance):
    #    cnt = 0
    #    while True:
    #        if cnt < 2:
    #            # First arm and leg movement
    #            self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.forearm, rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[0], rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[1], 270)
    #            self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.hand, rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[0], rotatePoint((self.x+100)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 45)[1], 270)
    #            for i in self.arm:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 330)
    #            self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.forearm2, rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[0], rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[1], 270)
    #            self.rotateFunctions[0 if self.forwardDir == "left" else 1](self.hand2, rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[0], rotatePoint((self.x+50)*0.5*scale - 8*scale, (self.y-20)*0.5*scale, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 110)[1], 270)
    #            for i in self.arm2:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 20)

    #            for i in [self.lowerleg, self.knee, self.feet]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+95)*0.5*scale, 90)
                
    #            for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 330)
    #            tk.update()
    #            time.sleep(0.5)
    #            cnt += 1
    #            if cnt >= distance:
    #                break
    #            # Second arm and leg movement
    #            for i in [self.lowerleg2, self.knee2, self.feet2]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y+95)*0.5*scale, 90)

    #            for i in [self.leg2, self.lowerleg2, self.knee2, self.feet2]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-18)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 300)

    #            for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 30)

    #            for i in self.arm:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 180)

    #            for i in self.arm2:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 280)
    #            tk.update()
    #            time.sleep(0.5)
    #            cnt += 1
    #            if cnt >= distance:
    #                break
    #        else:
    #            # Third arm and leg movement

    #            for i in [self.leg2, self.lowerleg2, self.knee2, self.feet2]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-18)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 120)

    #            for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 300)

    #            for i in self.arm:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 180)

    #            for i in self.arm2:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 160)
    #            for i in self.fullBody:
    #                canvas.move(i, 30*scale*0.5 if direction == "forward" else -30*scale*0.5, 0)
    #            self.x += 30 if direction == "forward" else -30
    #            tk.update()
    #            time.sleep(0.5)
    #            cnt += 1
    #            if cnt >= distance:
    #                break
    #            # Fourth arm and leg movement
    #            for i in [self.leg2, self.lowerleg2, self.knee2, self.feet2]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-18)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 240)

    #            for i in [self.lowerleg, self.leg1, self.knee, self.feet]:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+15)*0.5*scale, (self.y+70)*0.5*scale - 16*scale, 60)

    #            for i in self.arm:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x+30)*0.5*scale, (self.y-20)*0.5*scale, 180)

    #            for i in self.arm2:
    #                self.rotateFunctions[0 if self.forwardDir == "left" else 1](i, (self.x-20)*0.5*scale, (self.y-20)*0.5*scale, 200)
    #            for i in self.fullBody:
    #                canvas.move(i, 30*scale*0.5 if direction == "forward" else -30*scale*0.5, 0)
    #            self.x += 30 if direction == "forward" else -30
    #            tk.update()
    #            time.sleep(0.5)
    #            cnt += 1
    #            if cnt >= distance:
    #                break
    #    self.resetPos(cnt*30*scale*0.5 if direction == "forward" else cnt*-30*scale*0.5, 0)
    #    tk.update()
    #    time.sleep(0.1)
    #    self.x += 60 if direction == "forward" else -60

offenseP1 = character(1700*(1/12)*2, 850*(1/8)*2, "orange", "gold", "gray", "gold", "silver", True, "right")
offenseP2 = character(1700*(11/12)*2, 850*(1/8)*2, "orange", None, "black", "gray", "black", False, "left")

#def p1forward(event):
#    offenseP1.move("forward", 4)

#def p1backward(event):
#    offenseP1.move("backward", 4)

#def p2forward(event):
#    offenseP2.move("backward", 4)

#def p2backward(event):
#    offenseP2.move("forward", 4)

#canvas.bind_all("<Up>", p1forward)
#canvas.bind_all("<Down>", p1backward)
#canvas.bind_all("<w>", p2forward)
#canvas.bind_all("<s>", p2backward)

has_prev_key_release = None
holdCnt = 0

p1mvts = [offenseP1.mvt1, offenseP1.mvt2, offenseP1.mvt3, offenseP1.mvt4, offenseP1.mvt5]

def on_key_release(event): # runs once key is let go
    global has_prev_key_release
    has_prev_key_release = None
    global holdCnt
    holdCnt = 0

def on_key_press(event): # runs when key is pressed
    global holdCnt
    holdCnt += 1
    print(holdCnt, "on_key_press", repr(event.char))

def on_key_release_repeat(event): # runs while key is held
    global has_prev_key_release
    has_prev_key_release = tk.after_idle(on_key_release, event)
    print(holdCnt, "-", repr(event.char))

def on_key_press_repeat(event): # runs while key is held
    global has_prev_key_release
    if has_prev_key_release:
        global holdCnt
        holdCnt += 1
        tk.after_cancel(has_prev_key_release)
        has_prev_key_release = None
        print(holdCnt, "on_key_press_repeat", repr(event.char))
        if (holdCnt-1) % 3 == 0:
            p1mvts[((holdCnt-1)//3)%5-1]("forward" if event.keysym == "Up" else "backwards", 16)
            print("--------------->", ((holdCnt-1)//3)%5-1)
    else:
        on_key_press(event)

canvas.bind_all("<KeyPress-Up>", on_key_press_repeat)
canvas.bind_all("<KeyRelease-Up>", on_key_release_repeat)

canvas.bind_all("<KeyPress-Down>", on_key_press_repeat)
canvas.bind_all("<KeyRelease-Down>", on_key_release_repeat)

canvas.mainloop()
