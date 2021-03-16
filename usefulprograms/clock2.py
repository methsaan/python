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
    xRotationPoint = rotationPointCoords[0]
    yRotationPoint = rotationPointCoords[1]
    
    return rotatedCoords

canvas.create_oval(100, 100, 700, 700, fill="gray65", outline="black", width=25)
numCoords = [["XII", 400, 150], ["I", 500, 200], ["II", 600, 300], ["III", 650, 400], ["IV", 600, 500], ["V", 500, 600], ["VI", 400, 650], ["VII", 300, 600], ["VIII", 200, 500], ["IX", 150, 400], ["X", 200, 300], ["XI", 300, 200]]
for x in numCoords:
    canvas.create_text(x[1], x[2], text=x[0], font=("times", 30))

hourHand = canvas.create_polygon(390, 300, 410, 300, 410, 400, 390, 400)
minuteHand = canvas.create_polygon(395, 180, 405, 180, 405, 400, 395, 400)
secondHand = canvas.create_polygon(399, 180, 401, 180, 401, 400, 399, 400, fill="red")

canvas.create_oval(rotatePoint(500, 400, 400, 400, 10)[0], rotatePoint(500, 400, 400, 400, 10)[1], rotatePoint(500, 400, 400, 400, 10)[0]+10, rotatePoint(500, 400, 400, 400, 10)[1]+10, fill="black")
canvas.create_oval(rotatePoint(500, 400, 400, 400, 20)[0], rotatePoint(500, 400, 400, 400, 20)[1], rotatePoint(500, 400, 400, 400, 20)[0]+10, rotatePoint(500, 400, 400, 400, 20)[1]+10, fill="black")
canvas.create_oval(rotatePoint(500, 400, 400, 400, 30)[0], rotatePoint(500, 400, 400, 400, 30)[1], rotatePoint(500, 400, 400, 400, 30)[0]+10, rotatePoint(500, 400, 400, 400, 30)[1]+10, fill="black")
canvas.create_oval(rotatePoint(500, 400, 400, 400, 40)[0], rotatePoint(500, 400, 400, 400, 40)[1], rotatePoint(500, 400, 400, 400, 40)[0]+10, rotatePoint(500, 400, 400, 400, 40)[1]+10, fill="black")
canvas.create_oval(rotatePoint(500, 400, 400, 400, 50)[0], rotatePoint(500, 400, 400, 400, 50)[1], rotatePoint(500, 400, 400, 400, 50)[0]+10, rotatePoint(500, 400, 400, 400, 50)[1]+10, fill="black")
canvas.create_oval(rotatePoint(500, 400, 400, 400, 60)[0], rotatePoint(500, 400, 400, 400, 60)[1], rotatePoint(500, 400, 400, 400, 60)[0]+10, rotatePoint(500, 400, 400, 400, 60)[1]+10, fill="black")

#points = rotatePoints([[390, 300], [410, 300], [410, 400], [390, 400]])
#print(points)
#canvas.create_polygon(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1], points[3][0], points[3][1], fill="orange")

tk.update()
canvas.mainloop()
