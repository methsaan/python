#! /usr/bin/python3

import math
import time
import datetime
from tkinter import *
from itertools import chain

tk = Tk()
canvas = Canvas(tk, width=800, height=800, bg="#6699CC")
canvas.pack()

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

def rotate(obj, rotatex, rotatey, angle):
    oldCoords = []
    for x in range(0, len(canvas.coords(obj)), 2):
        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

canvas.create_oval(50, 50, 750, 750, fill="white", outline="black", width=40)

for x in range(12):
    canvas.create_text(rotatePoint(400, 120, 400, 400, 30*(x+1))[0], rotatePoint(400, 100, 400, 400, 30*(x+1))[1], text=str(x+1), font=("times new roman", 40))

hourHand = canvas.create_polygon(390, 240, 410, 240, 410, 410, 390, 410, fill="black")
minuteHand = canvas.create_polygon(395, 150, 405, 150, 405, 405, 395, 405, fill="black")
secondHand = canvas.create_polygon(399, 150, 401, 150, 401, 401, 399, 401, fill="red")

while True:
    canvas.coords(hourHand, 390, 240, 410, 240, 410, 410, 390, 410)
    canvas.coords(minuteHand, 395, 150, 405, 150, 405, 405, 395, 405)
    canvas.coords(secondHand, 399, 150, 401, 150, 401, 401, 399, 401)
    rotate(hourHand, 400, 400, datetime.datetime.now().hour%12*30 + datetime.datetime.now().minute*0.5)
    rotate(minuteHand, 400, 400, datetime.datetime.now().minute*6 + datetime.datetime.now().second*0.1)
    rotate(secondHand, 400, 400, datetime.datetime.now().second*6 + datetime.datetime.now().microsecond//10000*0.06)
    tk.update()

canvas.mainloop()
