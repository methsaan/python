#! /usr/bin/python3

import math
import random
import time
from tkinter import *

WIDTH = 900
HEIGHT = 900

class Tree:
    def __init__(self, width, height, treeObjSurface):
        self.width = width # square-based prism, length = width
        self.height = height
        self.volume = width**2 * height
        self.treeObjSurface = treeObjSurface # top of tree trunk
        self.downBound = canvas.coords(treeObjSurface)[5]
        self.upBound = canvas.coords(treeObjSurface)[3]
        self.rightBound = canvas.coords(treeObjSurface)[2]
        self.leftBound = canvas.coords(treeObjSurface)[0]

#class Field:

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

# Define quantities and units
widthInPx = 4*WIDTH/5
heightInPx = 4*HEIGHT/5
areaInPx = widthInPx * heightInPx
hectaresInWidth = random.randrange(3, 5)
hectaresInHeight = hectaresInWidth
widthOfHectareInPx = widthInPx/hectaresInWidth
heightOfHectareInPx = heightInPx/hectaresInHeight
areaInHectares = hectaresInWidth * hectaresInHeight

# Meter is defined unrealistically big relative to hectare for visualization purposes
# Trees are measured in meter unit while land is measured in hectare units
metersInWidth = hectaresInWidth*3
metersInHeight = metersInWidth
widthOfMeterInPx = widthInPx/metersInWidth
heightOfMeterInPx = widthOfMeterInPx

field = canvas.create_polygon(WIDTH/10, HEIGHT/10, 9*WIDTH/10, HEIGHT/10, 9*WIDTH/10, 9*HEIGHT/10, WIDTH/10, 9*HEIGHT/10, fill="green")

trees = []

numOfTrees = metersInWidth**2

for x in range(metersInWidth):
    for y in range(metersInWidth):
        w = widthOfMeterInPx*0.1 + random.random()*(widthOfMeterInPx*0.3)
        h = widthOfMeterInPx*random.randrange(2, 8)
        locationx = (WIDTH/10 + w/2) + (x+0.1)*widthOfMeterInPx + random.random()*widthOfMeterInPx*0.5
        locationy = (HEIGHT/10 + w/2) + (y+0.1)*widthOfMeterInPx + random.random()*widthOfMeterInPx*0.5
        trees.append(Tree(w, h, canvas.create_polygon(locationx-w/2, locationy-w/2, locationx+w/2, locationy-w/2, locationx+w/2, locationy+w/2, locationx-w/2, locationy+w/2, fill="brown", outline="black")))


canvas.mainloop()
