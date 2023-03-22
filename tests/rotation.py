#! /usr/bin/python3

import math
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()

def rotatePoint(x, y, rotatex, rotatey, angle):
    lengthFromRotPoint = math.sqrt(abs(x-rotatex)**2 + abs(y-rotatey)**2)
    angleStart = math.asin(abs(y-rotatey) / lengthFromRotPoint) * (180 / math.pi)
    if x < rotatex and y < rotatey:
        pass
    elif x > rotatex and y < rotatey:
        angleStart += 90
    elif x > rotatex and y > rotatey:
        angleStart += 180
    elif x < rotatex and y > rotatey:
        angleStart += 270
    elif x == rotatex and y > rotatey:
        angleStart = 270
    elif x == rotatex and y < rotatey:
        angleStart = 90
    elif x > rotatex and y == rotatey:
        angleStart = 180
    else:
        angleStart = 0
    print(angleStart)
    terminatingAngle = (angleStart + angle) % 360
    print(terminatingAngle)
    angleEnd = None
    if terminatingAngle >= 90 and terminatingAngle < 180:
        angleEnd = 180-terminatingAngle
    elif terminatingAngle >= 180 and terminatingAngle < 270:
        angleEnd = terminatingAngle-180
    elif terminatingAngle >= 270 and terminatingAngle < 360:
        angleEnd = 360-terminatingAngle
    else:
        angleEnd = terminatingAngle
    print(angleEnd)
    yFromRotPoint = abs(lengthFromRotPoint * math.sin(angleEnd))
    xFromRotPoint = abs(lengthFromRotPoint * math.cos(angleEnd) * (180/math.pi))
    print(xFromRotPoint, yFromRotPoint)
    newCoordx = 0
    newCoordy = 0
    if terminatingAngle >= 90 and terminatingAngle < 180:
        print("Second quadrant")
        newCoordx = rotatex + xFromRotPoint
        newCoordy = rotatey - yFromRotPoint
    elif terminatingAngle >= 180 and terminatingAngle < 270:
        print("Third quadrant")
        newCoordx = rotatex + xFromRotPoint
        newCoordy = rotatex + yFromRotPoint
    elif terminatingAngle >= 270 and terminatingAngle < 360:
        print("Fourth quadrant")
        newCoordx = rotatex - xFromRotPoint
        newCoordy = rotatey + yFromRotPoint
    else:
        print("First quadrant")
        newCoordx = rotatex - xFromRotPoint
        newCoordy = rotatey - yFromRotPoint
    return [newCoordx, newCoordy]

#def rotate(obj, rotatex, rotatey, angle):
#    oldCoords = []
#    for x in range(0, len(canvas.coords(obj)), 2):
#        oldCoords.append([canvas.coords(obj)[x], canvas.coords(obj)[x+1]])
#    print(oldCoords)
#    newCoords = []
#    for coords in oldCoords:
#        lengthFromRotPoint = math.sqrt(abs(coords[0]-rotatex)**2 + abs(coords[1]-rotatey)**2)
#        angleStart = math.atan(abs(coords[0]-rotatex) / abs(coords[1]-rotatey)) * (180 / math.pi)
#        angleEnd = 180 - angle - angleStart
#        yFromRotPoint = math.sin(angleEnd) * (180/math.pi) * lengthFromRotPoint
#        xFromRotPoint = math.sqrt(abs(lengthFromRotPoint**2 - yFromRotPoint**2))
#        newCoords.append(rotatex + xFromRotPoint)
#        newCoords.append(rotatey + yFromRotPoint)
#    canvas.coords(obj, *newCoords)

#box = canvas.create_polygon(200, 200, 300, 200, 300, 290, 200, 290, fill="red", outline="red")

#rotate(box, 300, 300, 80)

canvas.create_line(200, 200, 300, 300, width=3)
tk.update()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 10)[0], rotatePoint(200, 200, 300, 300, 10)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 20)[0], rotatePoint(200, 200, 300, 300, 20)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 30)[0], rotatePoint(200, 200, 300, 300, 30)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 40)[0], rotatePoint(200, 200, 300, 300, 40)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 50)[0], rotatePoint(200, 200, 300, 300, 50)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 60)[0], rotatePoint(200, 200, 300, 300, 60)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 70)[0], rotatePoint(200, 200, 300, 300, 70)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 80)[0], rotatePoint(200, 200, 300, 300, 80)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 90)[0], rotatePoint(200, 200, 300, 300, 90)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 100)[0], rotatePoint(200, 200, 300, 300, 100)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 110)[0], rotatePoint(200, 200, 300, 300, 110)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 120)[0], rotatePoint(200, 200, 300, 300, 120)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 130)[0], rotatePoint(200, 200, 300, 300, 130)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 140)[0], rotatePoint(200, 200, 300, 300, 140)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 150)[0], rotatePoint(200, 200, 300, 300, 150)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 160)[0], rotatePoint(200, 200, 300, 300, 160)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(200, 200, 300, 300, 170)[0], rotatePoint(200, 200, 300, 300, 170)[1], 300, 300, width=3)
tk.update()
print()
time.sleep(0.5)
canvas.create_line(rotatePoint(300, 400, 300, 300, 150)[0], rotatePoint(300, 400, 300, 300, 150)[1], 300, 300, width=3)
tk.update()

canvas.mainloop()
