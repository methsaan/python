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
        overlapping = False
        locationx = (WIDTH/10 + w/2) + random.random()*(4*WIDTH/5 - w)
        locationy = (HEIGHT/10 + w/2) + random.random()*(4*HEIGHT/5 - w)
        vicinityLeftBound = locationx - widthOfMeterInPx
        vicinityRightBound = locationx + widthOfMeterInPx
        vicinityUpBound = locationy - widthOfMeterInPx
        vicinityDownBound = locationy + widthOfMeterInPx
        tk.update()
        time.sleep(1)
        canvas.create_rectangle(vicinityLeftBound, vicinityUpBound, vicinityLeftBound+widthOfMeterInPx*2, vicinityUpBound+widthOfMeterInPx*2, width=2)
        tk.update()
        time.sleep(1)
        treesInVicinity = []
        for tree in trees:
            canvas.itemconfig(tree.treeObjSurface, fill="blue")
            tk.update()
            time.sleep(1)
            canvas.itemconfig(tree.treeObjSurface, fill="brown")
            tk.update()
            time.sleep(1)
            print("#", trees.index(tree))
            print("vicinity left", vicinityLeftBound)
            print("tree left", tree.leftBound)
            print("tree right", tree.rightBound)
            print("vicinity right", vicinityRightBound)
            print("vicinity up", vicinityUpBound)
            print("tree up", tree.upBound)
            print("tree down", tree.downBound)
            print("vicinity down", vicinityDownBound)
            temp = canvas.create_rectangle(tree.leftBound, tree.upBound, tree.rightBound, tree.downBound, fill="pink")
            temp2 = canvas.create_rectangle(vicinityLeftBound, vicinityUpBound, vicinityRightBound, vicinityDownBound, fill="orange", width=2)
            tk.update()
            time.sleep(2)
            canvas.itemconfig(temp, state="hidden")
            canvas.itemconfig(temp2, state="hidden")
            tk.update()
            if tree.leftBound > vicinityLeftBound and tree.rightBound < vicinityRightBound and\
               tree.upBound > vicinityUpBound and tree.downBound < vicinityDownBound:
                treesInVicinity.append(tree)
                canvas.itemconfig(tree.treeObjSurface, fill="brown")
                tk.update()
                time.sleep(1)
        for tree in treesInVicinity:
            if (((locationx + w/2) > tree.leftBound and (locationx + w/2) < tree.rightBound) and\
               (((locationy + w/2) > tree.upBound and (locationy + w/2) < tree.downBound) or\
               ((locationy - w/2) > tree.upBound and (locationy - w/2) < tree.downBound))) or\
               (((locationx - w/2) > tree.leftBound and (locationx - w/2) < tree.rightBound) and\
               (((locationy + w/2) > tree.upBound and (locationy + w/2) < tree.downBound) or\
               ((locationy - w/2) > tree.upBound and (locationy - w/2) < tree.downBound))):
                overlapping = True
                break
        if not overlapping:
            tk.update()
            time.sleep(1)
            break

    trees.append(Tree(w, h, canvas.create_polygon(locationx-w/2, locationy-w/2, locationx+w/2, locationy-w/2, locationx+w/2, locationy+w/2, locationx-w/2, locationy+w/2, fill="brown", outline="black")))

canvas.mainloop()
