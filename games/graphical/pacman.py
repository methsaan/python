#! /usr/bin/python3

import random
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=700, height=800)
canvas.pack()

GRID_SIZE = 5

print(100+5*(500/(GRID_SIZE)))

class point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.canvasX = 100+(coords[0]-1)*(500/GRID_SIZE)
        self.canvasY = 100+(coords[1]-1)*(500/GRID_SIZE)
    def getCanvasCoords(self):
        return [self.canvasX, self.canvasY]
    def getCoords(self):
        return [coords[0], coords[1]]

class line:
    def __init__(self, startCoords, endCoords):
        self.x = startCoords[0]
        self.y = startCoords[1]
        self.x2 = endCoords[0]
        self.y2 = endCoords[1]
        self.canvasX = 100+(startCoords[0]-1)*(500/GRID_SIZE)
        self.canvasY = 100+(startCoords[1]-1)*(500/GRID_SIZE)
        self.canvasX2 = 100+(endCoords[0]-1)*(500/GRID_SIZE)
        self.canvasY2 = 100+(endCoords[1]-1)*(500/GRID_SIZE)
    def getCanvasCoords(self):
        return [[self.canvasX, self.canvasY], [self.canvasX2, self.canvasY2]]
    def getCanvasReverseCoords(self):
        return [[self.canvasX2, self.canvasY2], [self.canvasX, self.canvasY]]
    def getCoords(self):
        return [[self.x, self.y], [self.x2, self.y2]]

class gridSpot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.canvasX = 100+(x+0.5)*(500/GRID_SIZE)
        self.canvasY = 100+(y+0.5)*(500/GRID_SIZE)
        self.spotsAttached = []
    def getCanvasCoords(self):
        return [self.canvasX, self.canvasY]
    def getCoords(self):
        return [self.x, self.y]
    def lineCoords(self, position):
        if position == "left":
            return [[self.canvasX-(250/GRID_SIZE), self.canvasY-(250/GRID_SIZE)], [self.canvasX-(250/GRID_SIZE), self.canvasY+(250/GRID_SIZE)]]
        elif position == "right":
            return [[self.canvasX+(250/GRID_SIZE), self.canvasY-(250/GRID_SIZE)], [self.canvasX+(250/GRID_SIZE), self.canvasY+(250/GRID_SIZE)]]
        elif position == "up":
            return [[self.canvasX-(250/GRID_SIZE), self.canvasY-(250/GRID_SIZE)], [self.canvasX+(250/GRID_SIZE), self.canvasY-(250/GRID_SIZE)]]
        elif position == "down":
            return [[self.canvasX-(250/GRID_SIZE), self.canvasY+(250/GRID_SIZE)], [self.canvasX+(250/GRID_SIZE), self.canvasY+(250/GRID_SIZE)]]
    def addSpotsAttached(self, spotsAttached):
        self.spotsAttached.append(spotsAttached)
    def getSpotsAttached(self):
        return self.spotsAttached

#def containsTopLeft(gridSpot):
#    for x in gridSpot.getSpotsAttached():
#        for y in x:
#            for z in y:


lines = []

for x in range(1, GRID_SIZE+1):
    lines.append(line([x, 1], [x+1, 1]))

for x in range(1, GRID_SIZE+1):
    lines.append(line([1, x], [1, x+1]))

for x in range(1, GRID_SIZE+1):
    lines.append(line([x, GRID_SIZE+1], [x+1, GRID_SIZE+1]))

for x in range(1, GRID_SIZE+1):
    lines.append(line([GRID_SIZE+1, x], [GRID_SIZE+1, x+1]))

cnt = 0

linesRemaining = []
for x in range(2, GRID_SIZE+1):
    for y in range(2, GRID_SIZE+1):
        startCoords = [x, y]
        if x == GRID_SIZE:
            if y == GRID_SIZE:
                endCoordOptions = [[startCoords[0], startCoords[1]+1], [startCoords[0], startCoords[1]-1], [startCoords[0]+1, startCoords[1]], [startCoords[0]-1, startCoords[1]]]
            else:
                endCoordOptions = [[startCoords[0], startCoords[1]-1], [startCoords[0]+1, startCoords[1]], [startCoords[0]-1, startCoords[1]]]
        else:
            if y == GRID_SIZE:
                endCoordOptions = [[startCoords[0], startCoords[1]+1], [startCoords[0], startCoords[1]-1], [startCoords[0]-1, startCoords[1]]]
            else:
                endCoordOptions = [[startCoords[0], startCoords[1]-1], [startCoords[0]-1, startCoords[1]]]
        for z in endCoordOptions:
            linesRemaining.append(line(startCoords, z))

tempLines = [linesRemaining[x] for x in range(len(linesRemaining))]
random.shuffle(tempLines)
tempLines = tempLines[:int(len(tempLines)*0.4)]

lineCoords = [tempLines[x].getCanvasCoords() for x in range(len(tempLines))] + [lines[x].getCanvasCoords() for x in range(len(lines))]
reverseLineCoords = [tempLines[x].getCanvasReverseCoords() for x in range(len(tempLines))] + [lines[x].getCanvasReverseCoords() for x in range(len(lines))]

for x in range(len(lines)):
    canvas.create_line(lines[x].getCanvasCoords()[0][0], lines[x].getCanvasCoords()[0][1], lines[x].getCanvasCoords()[1][0], lines[x].getCanvasCoords()[1][1], width=3)
    tk.update()
    time.sleep(0.01)

for x in range(len(tempLines)):
    canvas.create_line(tempLines[x].getCanvasCoords()[0][0], tempLines[x].getCanvasCoords()[0][1], tempLines[x].getCanvasCoords()[1][0], tempLines[x].getCanvasCoords()[1][1], width=3)
    tk.update()

gridSpots = []

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        g = gridSpot(x, y)
        canvas.create_oval(g.getCanvasCoords()[0]-2, g.getCanvasCoords()[1]-2, g.getCanvasCoords()[0]+2, g.getCanvasCoords()[1]+2, fill="black")
        tk.update()
        if g.lineCoords("left") not in lineCoords and g.lineCoords("left") not in reverseLineCoords:
            g.addSpotsAttached([x-1, y])
        if g.lineCoords("up") not in lineCoords and g.lineCoords("up") not in reverseLineCoords:
            g.addSpotsAttached([x, y-1])
        if g.lineCoords("right") not in lineCoords and g.lineCoords("right") not in reverseLineCoords:
            g.addSpotsAttached([x+1, y])
        if g.lineCoords("down") not in lineCoords and g.lineCoords("down") not in reverseLineCoords:
            g.addSpotsAttached([x, y+1])
        gridSpots.append(g)

for x in gridSpots:
    print(x.getCoords(), x.getSpotsAttached())
    

canvas.mainloop()
