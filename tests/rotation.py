#! /usr/bin/python3

import math
import time
from tkinter import *
from itertools import chain

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
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

box = canvas.create_polygon(200, 200, 300, 200, 300, 300, 200, 300, fill="red", outline="red")

rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()

canvas.mainloop()
ldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

box = canvas.create_polygon(200, 200, 300, 200, 300, 300, 200, 300, fill="red", outline="red")

rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()

canvas.mainloop()        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

box = canvas.create_polygon(200, 200, 300, 200, 300, 300, 200, 300, fill="red", outline="red")

rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()

canvas.mainloop()        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

box = canvas.create_polygon(200, 200, 300, 200, 300, 300, 200, 300, fill="red", outline="red")

rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()

canvas.mainloop()        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

box = canvas.create_polygon(200, 200, 300, 200, 300, 300, 200, 300, fill="red", outline="red")

rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()

canvas.mainloop()        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
    newCoords = []
    for x in oldCoords:
        newCoords.append([rotatePoint(x[0], x[1], rotatex, rotatey, angle)[0], rotatePoint(x[0], x[1], rotatex, rotatey, angle)[1]])
    canvas.coords(obj, *list(chain.from_iterable(newCoords)))

box = canvas.create_polygon(200, 200, 300, 200, 300, 300, 200, 300, fill="red", outline="red")

rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()
time.sleep(0.1)
rotate(box, 300, 300, 10)
tk.update()

canvas.mainloop()
