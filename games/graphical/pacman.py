#! /usr/bin/python3

from collections import defaultdict
import random
import time
from tkinter import *

scale = 1.4

tk = Tk()
canvas = Canvas(tk, width=350*scale, height=400*scale)
canvas.pack()

GRID_SIZE = 9

class Line:
    def __init__(self, startCoords, endCoords):
        self.x = startCoords[0]
        self.y = startCoords[1]
        self.x2 = endCoords[0]
        self.y2 = endCoords[1]
        self.canvasX = (50*scale)+(startCoords[0]-1)*((250*scale)/GRID_SIZE)
        self.canvasY = (50*scale)+(startCoords[1]-1)*((250*scale)/GRID_SIZE)
        self.canvasX2 = (50*scale)+(endCoords[0]-1)*((250*scale)/GRID_SIZE)
        self.canvasY2 = (50*scale)+(endCoords[1]-1)*((250*scale)/GRID_SIZE)
    def getCanvasCoords(self):
        return [[round(self.canvasX, 2), round(self.canvasY, 2)], [round(self.canvasX2, 2), round(self.canvasY2, 2)]]
    def getCanvasReverseCoords(self):
        return [[round(self.canvasX2, 2), round(self.canvasY2, 2)], [round(self.canvasX, 2), round(self.canvasY, 2)]]
    def getCoords(self):
        return [[self.x, self.y], [self.x2, self.y2]]

class GridSpot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.canvasX = (50*scale)+(x+0.5)*((250*scale)/GRID_SIZE)
        self.canvasY = (50*scale)+(y+0.5)*((250*scale)/GRID_SIZE)
        self.spotsAttached = []
    def getCanvasCoords(self):
        return [round(self.canvasX, 2), round(self.canvasY, 2)]
    def getCoords(self):
        return [self.x, self.y]
    def lineCoords(self, position):
        if position == "left":
            return [[round(self.canvasX-((scale*125)/GRID_SIZE), 2), round(self.canvasY-((scale*125)/GRID_SIZE), 2)], [round(self.canvasX-((scale*125)/GRID_SIZE), 2), round(self.canvasY+((scale*125)/GRID_SIZE), 2)]]
        elif position == "right":
            return [[round(self.canvasX+((scale*125)/GRID_SIZE), 2), round(self.canvasY-((scale*125)/GRID_SIZE), 2)], [round(self.canvasX+((scale*125)/GRID_SIZE), 2), round(self.canvasY+((scale*125)/GRID_SIZE), 2)]]
        elif position == "up":
            return [[round(self.canvasX-((scale*125)/GRID_SIZE), 2), round(self.canvasY-((scale*125)/GRID_SIZE), 2)], [round(self.canvasX+((scale*125)/GRID_SIZE), 2), round(self.canvasY-((scale*125)/GRID_SIZE), 2)]]
        elif position == "down":
            return [[round(self.canvasX-((scale*125)/GRID_SIZE), 2), round(self.canvasY+((scale*125)/GRID_SIZE), 2)], [round(self.canvasX+((scale*125)/GRID_SIZE), 2), round(self.canvasY+((scale*125)/GRID_SIZE), 2)]]
    def addSpotsAttached(self, spotsAttached):
        self.spotsAttached.append(spotsAttached)
    def getSpotsAttached(self):
        return self.spotsAttached

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.tempPath = []
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def storeAllPathsUtil(self, u, d, visited, path):
        visited[u] = True
        path.append(u)
        if u == d:
            self.tempPath.append([x for x in path])
        else:
            for x in self.graph[u]:
                if visited[x] == False:
                    self.storeAllPathsUtil(x, d, visited, path)
        path.pop()
        visited[u] = False
    def storeAllPaths(self, s, d):
        visited = [False]*self.V
        path = []
        self.storeAllPathsUtil(s, d, visited, path)
    def getPaths(self):
        return self.tempPath
    def clearPaths(self):
        self.tempPath = []

lines = []

for x in range(1, GRID_SIZE+1):
    lines.append(Line([x, 1], [x+1, 1]))

for x in range(1, GRID_SIZE+1):
    lines.append(Line([1, x], [1, x+1]))

for x in range(1, GRID_SIZE+1):
    lines.append(Line([x, GRID_SIZE+1], [x+1, GRID_SIZE+1]))

for x in range(1, GRID_SIZE+1):
    lines.append(Line([GRID_SIZE+1, x], [GRID_SIZE+1, x+1]))

mazeLines = []
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
            mazeLines.append(Line(startCoords, z))

allLines = [mazeLines[x] for x in range(len(mazeLines))]
random.shuffle(allLines)

def gridSpotByCoords(coords):
    for x in gridSpots:
        if x[0].getCoords() == coords:
            return x
    return gridSpots[0]

def gridSpotAdjacent(a, b):
    if abs(a-b) == 1 and a//GRID_SIZE == b//GRID_SIZE:
        lineBetween = (gridSpots[a][0].lineCoords("up") if b < a else gridSpots[a][0].lineCoords("down"))
        if lineBetween not in lineCoords and lineBetween not in reverseLineCoords:
            return True
    elif abs(a-b) == GRID_SIZE:
        lineBetween = (gridSpots[a][0].lineCoords("left") if b < a else gridSpots[a][0].lineCoords("right"))
        if lineBetween not in lineCoords and lineBetween not in reverseLineCoords:
            return True
    return False

def gridSpotBlockAdjacent(a, l):
    for x in l:
        if gridSpotAdjacent(a, x):
            return True
    return False

allLines = allLines[:int(len(allLines)*0.4)]

lineCoords = [allLines[x].getCanvasCoords() for x in range(len(allLines))] + [lines[x].getCanvasCoords() for x in range(len(lines))]
reverseLineCoords = [allLines[x].getCanvasReverseCoords() for x in range(len(allLines))] + [lines[x].getCanvasReverseCoords() for x in range(len(lines))]

gridSpots = []
idxNumTemp = 0

trappedSpots = []

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        g = GridSpot(x, y)
        tk.update()
        if g.lineCoords("left") not in lineCoords and g.lineCoords("left") not in reverseLineCoords:
            g.addSpotsAttached([x-1, y])
        if g.lineCoords("up") not in lineCoords and g.lineCoords("up") not in reverseLineCoords:
            g.addSpotsAttached([x, y-1])
        if g.lineCoords("right") not in lineCoords and g.lineCoords("right") not in reverseLineCoords:
            g.addSpotsAttached([x+1, y])
        if g.lineCoords("down") not in lineCoords and g.lineCoords("down") not in reverseLineCoords:
            g.addSpotsAttached([x, y+1])
        gridSpots.append((g, idxNumTemp))
        idxNumTemp += 1

graph = Graph(GRID_SIZE**2)

for x in gridSpots:
    for y in x[0].getSpotsAttached():
        graph.addEdge(x[1], gridSpotByCoords(y)[1])

trappedSpots = []

for x in gridSpots:
    graph.storeAllPaths(0, x[1])
    if len(graph.getPaths()) == 0:
        trappedSpots.append(x[1])
    graph.clearPaths()

trappedGroups = []

for x in trappedSpots:
    blocksAdjacent = False
    for y in trappedGroups:
        if gridSpotBlockAdjacent(x, y):
            y.append(x)
            blocksAdjacent = True
    if blocksAdjacent == False:
        trappedGroups.append([x])

for x in trappedGroups:
    for y in x:
        for z in trappedGroups:
            if z != x and y in z:
                z.remove(y)
                x += z
                trappedGroups.remove(z)

untrappedGroup = []

for x in gridSpots:
    if not any([x[1] in i for i in trappedGroups]):
        untrappedGroup.append(x[1])

print("trapped")
print(trappedGroups)
print("untrapped")
print(untrappedGroup)

print("trapped groups")
for x in trappedGroups:
    print(x)

# adjacent spots
print("trapped groups individual")
for x in trappedGroups:
    for y in x:
        adjacentSpotNums = [y-GRID_SIZE if y-GRID_SIZE >= 0 else None, y+GRID_SIZE if y+GRID_SIZE <= GRID_SIZE**2-1 else None, y-1 if (y-1)%GRID_SIZE != GRID_SIZE-1 else None, y+1 if (y+1)%GRID_SIZE != 0 else None]
        print(y, end=" -> ")
        print(adjacentSpotNums)
    print()

colors = ["red", "orange", "yellow", "green", "blue", "white", "brown", "aqua", "purple", "pink", "magenta", "beige", "gray"]
random.shuffle(colors)
colors = colors[:len(trappedGroups)]

for x in range(len(lines)):
    canvas.create_line(lines[x].getCanvasCoords()[0][0], lines[x].getCanvasCoords()[0][1], lines[x].getCanvasCoords()[1][0], lines[x].getCanvasCoords()[1][1], width=3)
    tk.update()
    time.sleep(0.01)

for x in range(len(allLines)):
    canvas.create_line(allLines[x].getCanvasCoords()[0][0], allLines[x].getCanvasCoords()[0][1], allLines[x].getCanvasCoords()[1][0], allLines[x].getCanvasCoords()[1][1], width=3)
    tk.update()

for x in gridSpots:
    color = None
    if x[1] in trappedSpots:
        for y in range(len(trappedGroups)):
            if x[1] in trappedGroups[y]:
                color = colors[y]
    if color == None:
        canvas.create_oval(x[0].getCanvasCoords()[0]-2, x[0].getCanvasCoords()[1]-2, x[0].getCanvasCoords()[0]+2, x[0].getCanvasCoords()[1]+2, fill="black")
    else:
        canvas.create_rectangle(x[0].getCanvasCoords()[0]-15, x[0].getCanvasCoords()[1]-15, x[0].getCanvasCoords()[0]+15, x[0].getCanvasCoords()[1]+15, fill=color, outline=color)
    tk.update()

canvas.mainloop()
