#! /usr/bin/python3

WIDTH = 1500
HEIGHT = 900

import math
import time
from itertools import chain
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=WIDTH+400, height=HEIGHT)
canvas.pack()

shapeCoordsCam1 = []
shapeCreated = False

shapeCam1 = None
areaCam1Txt = canvas.create_text(WIDTH*0.5, HEIGHT*0.65, text="Area on side camera: 0px\u00B2", font=("helvetica", 25))
screenCam1 = canvas.create_rectangle(WIDTH*0.25, HEIGHT*0.1, WIDTH*0.75, HEIGHT*0.6, fill="white")
imageCam2 = canvas.create_polygon(WIDTH*0.45, HEIGHT*0.85, WIDTH*0.55, HEIGHT*0.85, WIDTH*0.55, HEIGHT*0.9, WIDTH*0.45, HEIGHT*0.9)
frontAngleFromSide = 0
sliderBg = canvas.create_rectangle(WIDTH*0.3, HEIGHT*0.025, WIDTH*0.7, HEIGHT*0.075)
slider = canvas.create_rectangle(WIDTH*0.48, HEIGHT*0.02, WIDTH*0.52, HEIGHT*0.08, fill="white")
sliderTxt = canvas.create_text(WIDTH*0.5, HEIGHT*0.05, text="0\u00B0", font=("helvetica", 20))
screenCam2 = canvas.create_rectangle(WIDTH+400*0.1, HEIGHT*0.1, WIDTH+400*0.9, HEIGHT*(0.1 + (16/75)), fill="white")

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

def shapeArea(points):
    x1, x2, x3, y1, y2, y3 = points[0][0], points[1][0], points[2][0], points[0][1], points[1][1], points[2][1]
    side1 = math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)
    side2 = math.sqrt(abs(x3-x1)**2 + abs(y3-y1)**2)
    side3 = math.sqrt(abs(x3-x2)**2 + abs(y3-y2)**2)
    semiperimeter = (side1+side2+side3)/2
    return math.sqrt(semiperimeter*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3))

def createShapeCam1():
    global shapeCam1
    global areaCam1Txt
    global shapeCreated
    global shapeCoordsCam1
    if not shapeCreated and len(shapeCoordsCam1) > 2:
        shapeCoordsUnpacked = []
        for x in range(len(shapeCoordsCam1)):
            for y in range(2):
                shapeCoordsUnpacked.append(shapeCoordsCam1[x][y])
        shapeCam1 = canvas.create_polygon(*shapeCoordsUnpacked)
        shapeCreated = True
        canvas.itemconfig(areaCam1Txt, text=("Area on side view camera: " + str(round(shapeArea(shapeCoordsCam1), 2)) + "px\u00B2"))

def addCoord(event):
    global shapeCoordsCam1
    if len(shapeCoordsCam1) < 2:
        shapeCoordsCam1.append((event.x, event.y))
    else:
        shapeCoordsCam1.append((event.x, event.y))
        createShapeCam1()

def changeAngle(event):
    global imageCam2
    global frontAngleFromSide
    global slider
    global sliderTxt
    if event.keysym == "Left":
        if frontAngleFromSide > -90:
            frontAngleFromSide -= 1
            rotate(imageCam2, WIDTH*0.5, HEIGHT*0.2, 1)
            canvas.move(slider, -WIDTH*0.4/180, 0)
            canvas.move(sliderTxt, -WIDTH*0.4/180, 0)
            canvas.itemconfig(sliderTxt, text=(str(frontAngleFromSide) + "\u00B0"))
    elif event.keysym == "Right":
        if frontAngleFromSide < 90:
            frontAngleFromSide += 1
            rotate(imageCam2, WIDTH*0.5, HEIGHT*0.2, -1)
            canvas.move(slider, WIDTH*0.4/180, 0)
            canvas.move(sliderTxt, WIDTH*0.4/180, 0)
            canvas.itemconfig(sliderTxt, text=(str(frontAngleFromSide) + "\u00B0"))

canvas.tag_bind(screenCam1, "<Button-1>", addCoord)
canvas.bind_all('<KeyPress-Left>', changeAngle)
canvas.bind_all('<KeyPress-Right>', changeAngle)



canvas.mainloop()
