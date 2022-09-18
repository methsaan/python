#! /usr/bin/python3

import random
import time
from tkinter import *

scale = 1

tk = Tk()
canvas = Canvas(tk, width=350*scale, height=400*scale)
canvas.pack()

GRID_SIZE = 6

print((50*scale)+6*((250*scale)/(GRID_SIZE)))

#class nonbinaryTree:
#    def __init__(self, root):
        #self.treeArr = [ [29, [[28, []], [21, []]]] ]
#        self.treeArr = [[root, []]]
#    def addChildren(self, children, row):
#        treeArr = [ [29, []] ]
        # add children to row 1, 29
#        treeArr[0][1].append([28, []])
#        treeArr[0][1].append([21, []])
        # add children to row 2, 29->28
#        treeArr[0][1][0][1].append([27, []])
#        treeArr[0][1][0][1].append([20, []])
        # add children to row 2, 29->21
#        treeArr[0][1][1][1].append([22, []])
        # add children to row 2, 29->21->22
#        treeArr[0][1][1][1][1].append([30, []])
#        [[29, [[28, [[27, []], [20, [[12, [[4, []], [13, []]]]]]]], [21, [[22, [[30, []]]]]]]]]
#        29 (row 1): treeArr[0][0] 0, 0
#        28 (row 2): treeArr[0][1][0][0] 0, 1 0, 0
#        21 (row 2): treeArr[0][1][1][0] 0, 1 1, 0
#        27 (row 3): treeArr[0][1][0][1][0] 0, 1 0 1, 0
#        20 (row 3): treeArr[0][1][0][1][1] 0, 1 0 1, 1
#        22 (row 3): treeArr[0][1][1][1][0] 0, 1 1 1, 0
#        12 (row 4): treeArr[0][1][0][1][1][1][0] 0, 1 0 1 1 1, 0
#        04 (row 5): treeArr[0][1][0][1][1][1][1][0][0]
#        13 (row 5): treeArr[0][1][0][1][1][1][1][1][0]
#
#    def getRowVals(self, row):
#        arr = []
#        binCode = 
#
#        return arr
#        exec("self.treeArr[0]" + 
        # 29: treeArr[0][0]
        # 28: treeArr[0][1][0][0]
        # 21: treeArr[0][1][1][0]
        # 20: treeArr[0][1][0][1][0]
        # 27: treeArr[0][1][0][1][1]
        # 32: treeArr[0][1][1][1][2]
        # 22: treeArr[0][1][1][1][0]

#for x in gridSpots:
#    print(x.getCoords(), ">", x.getSpotsAttached())

#pathsTree = nonbinaryTree(gridSpots[15].getCoords())

#while True:
    
#    pathsTree.addChildren(gridSpots[15].getSpotsAttached())


class point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.canvasX = (50*scale)+(coords[0]-1)*((250*scale)/GRID_SIZE)
        self.canvasY = (50*scale)+(coords[1]-1)*((250*scale)/GRID_SIZE)
    def getCanvasCoords(self):
        return [round(self.canvasX, 2), round(self.canvasY, 2)]
    def getCoords(self):
        return [coords[0], coords[1]]

class line:
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

class gridSpot:
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
    print(x.getCoords(), ">", x.getSpotsAttached())

def containsTopLeftPath(grid, gridSpotItem, checked):
    print(gridSpotItem.getCoords())
    print()
    if [0, 0] in gridSpotItem.getSpotsAttached():
        print("True")
        return True
    else:
        print("False")
        for y in grid:
            print("coords in grid: (y)", y.getCoords())
            if y.getCoords() in gridSpotItem.getSpotsAttached() and y.getCoords() not in checked:
                print("\tFound in grid spot: (y, spots attached)", y.getCoords(), y.getSpotsAttached())
                checked.append(y.getCoords())
                return containsTopLeftPath(grid, y, checked)
        return False


#def addToPath(grid, gridSpotItem, paths):
#    paths.append(gridSpotItem.getSpotsAttached())
#    return paths

#def fullPath(grid, gridSpotItem, paths, fullPaths):




#print(">", containsTopLeftPath(gridSpots, gridSpots[15], []))

#for x in gridSpots:
#    print(">", x.getCoords(), containsTopLeftPath(gridSpots, x))

canvas.mainloop()
