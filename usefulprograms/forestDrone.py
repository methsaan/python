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
        self.downBound = canvas.coords(treeObjSurface)[2]
        self.upBound = canvas.coords(treeObjSurface)[0]
        self.rightBound = canvas.coords(treeObjSurface)[5]
        self.leftBound = canvas.coords(treeObjSurface)[1]

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

# Define quantities and units
widthInPx = 4*WIDTH/5
print("widthInPx:", widthInPx)
heightInPx = 4*HEIGHT/5
print("heightInPx:", heightInPx)
areaInPx = widthInPx * heightInPx
print("areaInPx:", areaInPx)
hectaresInWidth = random.randrange(4, 8)
print("hectaresInWidth:", hectaresInWidth)
hectaresInHeight = hectaresInWidth
print("hectaresInHeight:", hectaresInHeight)
widthOfHectareInPx = widthInPx/hectaresInWidth
print("widthOfHectareInPx:", widthOfHectareInPx)
heightOfHectareInPx = heightInPx/hectaresInHeight
print("heightOfHectareInPx:", heightOfHectareInPx)
areaInHectares = hectaresInWidth * hectaresInHeight
print("areaInHectares:", areaInHectares)

# Meter is defined unrealistically big relative to hectare for visualization purposes
# Trees are measured in meter unit while land is measured in hectare units
metersInWidth = hectaresInWidth*3
print("metersInWidth:", metersInWidth)
metersInHeight = metersInWidth
print("metersInHeight:", metersInHeight)
widthOfMeterInPx = widthInPx/metersInWidth
print("widthOfMeterInPx:", widthOfMeterInPx)
heightOfMeterInPx = widthOfMeterInPx
print("heightOfMeterInPx:", heightOfMeterInPx)

field = canvas.create_polygon(WIDTH/10, HEIGHT/10, 9*WIDTH/10, HEIGHT/10, 9*WIDTH/10, 9*HEIGHT/10, WIDTH/10, 9*HEIGHT/10, fill="green")

trees = []

numOfTrees = 400#random.randrange(5, 10)

cnt = 0
for x in range(numOfTrees):
    w = widthOfMeterInPx*0.2 + random.random()*(widthOfMeterInPx*0.5)
    h = widthOfMeterInPx*random.randrange(2, 8)
    locationx = (WIDTH/10 + w/2) + random.random()*(4*WIDTH/5 - w)
    locationy = (HEIGHT/10 + w/2) + random.random()*(4*HEIGHT/5 - w)
    while True:
        inPath = False
        for prevTree in trees:
            print("Tree #", trees.index(prevTree), "New tree:", x)
            if not (((locationx - w/2) > prevTree.rightBound or (locationx + w/2) < prevTree.leftBound) and\
               ((locationy - w/2) > prevTree.downBound or (locationy + w/2) < prevTree.upBound)):
                inPath = True
                cnt += 1
                break
        if not inPath:
            time.sleep(0.01)
            tk.update()
            break
        locationx = (WIDTH/10 + w/2) + random.random()*(4*WIDTH/5 - w)
        locationy = (HEIGHT/10 + w/2) + random.random()*(4*HEIGHT/5 - w)

    trees.append(Tree(w, h, canvas.create_polygon(locationx-w/2, locationy-w/2, locationx+w/2, locationy-w/2, locationx+w/2, locationy+w/2, locationx-w/2, locationy+w/2, fill="brown", outline="black")))

canvas.mainloop()
