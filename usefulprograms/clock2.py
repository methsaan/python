#! /usr/bin/python3

import datetime
import time
import math
import decimal
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800, bg="tan3")
canvas.pack()

def rotatePoint(x, y, xRot, yRot, angle):
    x1 = math.cos(angle * (math.pi / 180)) * (x - xRot) - math.sin(angle * (math.pi / 180)) * (y - yRot) + xRot
    y1 = math.sin(angle * (math.pi / 180)) * (x - xRot) - math.cos(angle * (math.pi / 180)) * (y - yRot) + yRot
    return [x1, y1]

def rotatePoints(coordsList, rotationPointCoords, angle):
    rotatedCoords = []
    for x in range(0, len(coordsList), 2):
        rotatedCoords.append(rotatePoint(coordsList[x], coordsList[x+1], rotationPointCoords[0], rotationPointCoords[1], angle)[0])
        rotatedCoords.append(rotatePoint(coordsList[x], coordsList[x+1], rotationPointCoords[0], rotationPointCoords[1], angle)[1])

    return rotatedCoords

canvas.create_oval(100, 100, 700, 700, fill="gray65", outline="black", width=25)
numCoords = [["XII", 400, 150], ["I", 500, 200], ["II", 600, 300], ["III", 650, 400], ["IV", 600, 500], ["V", 500, 600], ["VI", 400, 650], ["VII", 300, 600], ["VIII", 200, 500], ["IX", 150, 400], ["X", 200, 300], ["XI", 300, 200]]
for x in numCoords:
    canvas.create_text(x[1], x[2], text=x[0], font=("times", 30))

hourHand = canvas.create_polygon(390, 300, 410, 300, 410, 400, 390, 400)
minuteHand = canvas.create_polygon(395, 180, 405, 180, 405, 400, 395, 400)
secondHand = canvas.create_polygon(399, 180, 401, 180, 401, 400, 399, 400, fill="red")

# test out rotate points

canvas.mainloop()
