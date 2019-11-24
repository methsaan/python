#! /usr/bin/python3

import subprocess as sp

def isLinear(*nums):
    difference = 0
    differenceList = []
    for x in range(len(nums)-1):
        difference = nums[x]-nums[x+1]
        differenceList.append(difference)
    for x in range(1, len(differenceList)):
        if differenceList[x] != differenceList[x-1]:
            return False
    return True

def filled(filllist, char):
    fill = True
    for x in filllist:
        if x != char:
            fill = False
            break
    return fill

grid = ((" ", " ", " "), (" ", " ", " "), (" ", " ", " "))
while True:
    sp.call("clear", shell=True)
    print("_______________________________")
    print("|         |         |         |")
    print("|    %s    |    %s    |    %s    |" % (grid[0][0], grid[0][1], grid[0][2]))
    print("|_________|_________|_________|")
    print("|         |         |         |")
    print("|    %s    |    %s    |    %s    |" % (grid[1][0], grid[1][1], grid[1][2]))
    print("|_________|_________|_________|")
    print("|         |         |         |")
    print("|    %s    |    %s    |    %s    |" % (grid[2][0], grid[2][1], grid[2][2]))
    print("|_________|_________|_________|")
    x = input("Enter position (X): ")
    position = [0, 0]
    if x.split(" ")[0] == "top":
        position[0] = 0
    elif x.split(" ")[0] == "middle":
        position[0] = 1
    else:
        position[0] = 2
    if x.split(" ")[1] == "left":
        position[1] = 0
    elif x.split(" ")[1] == "middle":
        position[1] = 1
    else:
        position[1] = 2
    grid = list(grid)
    for x in range(len(grid)):
        grid[x] = list(grid[x])
    grid[position[0]][position[1]] = "X"
    for x in range(len(grid)):
        grid[x] = tuple(grid[x])
    grid = tuple(grid)
    filledHoriz = False
    for x in grid:
        if filled(x, "X"):
            filledHoriz = True
            break
    xPos = []
    xPos2 = []
    xPos3 = []
    for x in grid:
        if "X" in x:
            positions = [i for i, n in enumerate(x) if n == 'X'] + [4, 4]
            xPos.append(x.index("X"))
            xPos2.append(positions[1])
            xPos3.append(positions[2])
        else:
            xPos.append(4)
            xPos2.append(4)
            xPos3.append(4)
    filledVertOrDiag = (isLinear(*xPos) and 4 not in xPos) or (isLinear(*xPos2) and 4 not in xPos2) or (isLinear(*xPos3) and 4 not in xPos3)
    sp.call("clear", shell=True)
    if filledVertOrDiag:
        print("X is filled vertically or diagonally")
    if filledHoriz:
        print("X is filled horizontally");
    print("_______________________________")
    print("|         |         |         |")
    print("|    %s    |    %s    |    %s    |" % (grid[0][0], grid[0][1], grid[0][2]))
    print("|_________|_________|_________|")
    print("|         |         |         |")
    print("|    %s    |    %s    |    %s    |" % (grid[1][0], grid[1][1], grid[1][2]))
    print("|_________|_________|_________|")
    print("|         |         |         |")
    print("|    %s    |    %s    |    %s    |" % (grid[2][0], grid[2][1], grid[2][2]))
    print("|_________|_________|_________|")
    o = input("Enter position (O): ")
    position = [0, 0]
    if o.split(" ")[0] == "top":
        position[0] = 0
    elif o.split(" ")[0] == "middle":
        position[0] = 1
    else:
        position[0] = 2
    if o.split(" ")[1] == "left":
        position[1] = 0
    elif o.split(" ")[1] == "middle":
        position[1] = 1
    else:
        position[1] = 2
    grid = list(grid)
    for x in range(len(grid)):
        grid[x] = list(grid[x])
    grid[position[0]][position[1]] = "O"
    for x in range(len(grid)):
        grid[x] = tuple(grid[x])
    grid = tuple(grid)
    filledHoriz = False
    for x in grid:
        if filled(x, "O"):
            filledHoriz = True
            break
    xPos = []
    xPos2 = []
    xPos3 = []
    for x in grid:
        if "X" in x:
            positions = [i for i, n in enumerate(x) if n == 'X'] + [4, 4]
            xPos.append(x.index("X"))
            xPos2.append(positions[1])
            xPos3.append(positions[2])
        else:
            xPos.append(4)
            xPos2.append(4)
            xPos3.append(4)
    filledVertOrDiag = isLinear(*xPos)
