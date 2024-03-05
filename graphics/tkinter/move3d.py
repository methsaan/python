#! /usr/bin/python3

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
    def getCanvasCoords(self):
        xCoord = 400 - self.x*(20/math.sqrt(2)) + self.y*20 
        yCoord = 400 + self.x*(20/math.sqrt(2)) - self.z*20
        return xCoord, yCoord

class Vector:
    def __init__(self, pCoords1, pCoords2):
        self.p1 = Point(*pCoords1)
        self.p2 = Point(*pCoords2)
        self.points = [self.p1, self.p2]
    def translate(self, xShift, yShift, zShift):
        for x in range(len(self.points)):
            self.points[x].move(xShift, yShift, zShift)
    def getCanvasCoords(self):
        return self.p1.getCanvasCoords(), self.p2.getCanvasCoords()

class Object3d:
    def __init__(self, vectors):
        self.vectors = vectors
    def getEdges(self):
        return self.vectors
    def translate(self, xMove, yMove, zMove):
        for x in range(len(self.vectors)):
            self.vectors[x].translate(xMove, yMove, zMove)
    def getCanvasCoords(self):
        return [x.getCanvasCoords() for x in self.vectors]

import time
import math

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()

canvas.create_line(0, 800, 800, 0)
canvas.create_line(0, 400, 800, 400)
canvas.create_line(400, 0, 400, 800)

for x in range(40):
    canvas.create_line(x*20, 390, x*20, 410)
    canvas.create_line(390, x*20, 410, x*20)

for x in range(28):
    canvas.create_line(390-x*(20/math.sqrt(2)), 400+x*(20/math.sqrt(2)), 410-x*(20/math.sqrt(2)), 400+x*(20/math.sqrt(2)))

for x in range(1, 28):
    canvas.create_line(390+x*(20/math.sqrt(2)), 400-x*(20/math.sqrt(2)), 410+x*(20/math.sqrt(2)), 400-x*(20/math.sqrt(2)))
'''
edges = [Vector((0, 0, 0), (0, 5, 0)), Vector((0, 0, 0), (5, 0, 0)),\
         Vector((5, 0, 0), (5, 5, 0)), Vector((5, 5, 0), (0, 5, 0)),\
         Vector((0, 0, 0), (0, 0, 5)), Vector((0, 0, 5), (0, 5, 5)),\
         Vector((0, 5, 5), (0, 5, 0)), Vector((0, 0, 5), (5, 0, 5)),\
         Vector((5, 0, 5), (5, 5, 5)), Vector((5, 5, 5), (0, 5, 5)),\
         Vector((5, 0, 0), (5, 0, 5)), Vector((5, 5, 5), (5, 5, 0))]
'''
edges = [Vector((0, 0, 0), (0, -5, 0)), Vector((0, 0, 0), (-5, 0, 0)),\
         Vector((-5, 0, 0), (-5, -5, 0)), Vector((-5, -5, 0), (0, -5, 0)),\
         Vector((0, 0, 0), (1, 1, -5)), Vector((1, 1, -5), (1, -6, -5)),\
         Vector((1, -6, -5), (0, -5, 0)), Vector((1, 1, -5), (-6, 1, -5)),\
         Vector((-6, 1, -5), (-6, -6, -5)), Vector((-6, -6, -5), (1, -6, -5)),\
         Vector((-5, 0, 0), (-6, 1, -5)), Vector((-6, -6, -5), (-5, -5, 0))]

cube = Object3d(edges)

canvEdges = []

for i in cube.getEdges():
    aCoords, bCoords = i.getCanvasCoords()
    canvEdges.append(canvas.create_line(*aCoords, *bCoords, width=2, fill="blue"))

for x in range(17):
    cube.translate(1, 0, 0)
    for i in range(len(cube.getEdges())):
         aCoords, bCoords = cube.getCanvasCoords()[i]
         canvas.coords(canvEdges[i], *aCoords, *bCoords)
    tk.update()
    time.sleep(0.01)

for x in range(19):
    cube.translate(0, 1, 0)
    for i in range(len(cube.getEdges())):
         aCoords, bCoords = cube.getCanvasCoords()[i]
         canvas.coords(canvEdges[i], *aCoords, *bCoords)
    tk.update()
    time.sleep(0.01)

for x in range(18):
    cube.translate(0, 0, 1)
    for i in range(len(cube.getEdges())):
         aCoords, bCoords = cube.getCanvasCoords()[i]
         canvas.coords(canvEdges[i], *aCoords, *bCoords)
    tk.update()
    time.sleep(0.01)

for n in range(2):
    for x in range(18):
        cube.translate(0, 0, -1)
        for i in range(len(cube.getEdges())):
            aCoords, bCoords = cube.getCanvasCoords()[i]
            canvas.coords(canvEdges[i], *aCoords, *bCoords)
        tk.update()
        time.sleep(0.01)
    for x in range(19):
        cube.translate(0, -1, 0)
        for i in range(len(cube.getEdges())):
            aCoords, bCoords = cube.getCanvasCoords()[i]
            canvas.coords(canvEdges[i], *aCoords, *bCoords)
        tk.update()
        time.sleep(0.01)
    for x in range(17):
        cube.translate(-1, 0, 0)
        for i in range(len(cube.getEdges())):
            aCoords, bCoords = cube.getCanvasCoords()[i]
            canvas.coords(canvEdges[i], *aCoords, *bCoords)
        tk.update()
        time.sleep(0.01)

canvas.mainloop()
