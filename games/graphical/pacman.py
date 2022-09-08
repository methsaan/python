#! /usr/bin/python3

import random
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=700, height=800)
canvas.pack()

class point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.canvasX = 100+(coords[0]-1)*50
        self.canvasY = 100+(coords[1]-1)*50
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
        self.canvasX = 100+(startCoords[0]-1)*50
        self.canvasY = 100+(startCoords[1]-1)*50
        self.canvasX2 = 100+(endCoords[0]-1)*50
        self.canvasY2 = 100+(endCoords[1]-1)*50
    def getCanvasCoords(self):
        return [[self.canvasX, self.canvasY], [self.canvasX2, self.canvasY2]]
    def getCoords(self):
        return [[self.x, self.y], [self.x2, self.y2]]

lines = []
tempLinesCoords = []

for x in range(1, 10):
    lines.append(line([x, 1], [x+1, 1]))

for x in range(1, 10):
    lines.append(line([1, x], [1, x+1]))

for x in range(1, 10):
    lines.append(line([x, 10], [x+1, 10]))

for x in range(1, 10):
    lines.append(line([10, x], [10, x+1]))

l = line([2, 2], [2, 3])
f = line([2, 2], [2, 3])
d = line([2, 3], [2, 4])

for x in tempLinesCoords:
    print(x)

print()
print()

for x in range(200):
    while True:
        startCoords = [random.randrange(2, 10), random.randrange(2, 10)]
        endCoords = random.choice([[startCoords[0], startCoords[1]+1], [startCoords[0], startCoords[1]-1], [startCoords[0]+1, startCoords[1]], [startCoords[0]-1, startCoords[1]]])
        l = line(startCoords, endCoords)
        if l.getCoords() not in tempLinesCoords:
            tempLinesCoords.append(l.getCoords())
            lines.append(l)
            print(l.getCoords())

for x in range(200):
    canvas.create_line(lines[x].getCanvasCoords()[0][0], lines[x].getCanvasCoords()[0][1], lines[x].getCanvasCoords()[1][0], lines[x].getCanvasCoords()[1][1])
    tk.update()
    time.sleep(0.05)

canvas.mainloop()
