#! /usr/bin/python3

import subprocess as sp

def isLinear(*nums):
    difference = 0
    differenceList = []
    for x in range(len(nums)-1):
        difference = abs(nums[x]-nums[x+1])
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

def hasLinearChar(multidlist, char):
    pos = []
    c1 = False
    c2 = False
    for x in multidlist:
        pos.append(list(x).index(char))
    if isLinear(*pos):
        c1 = True
    for x in range(len(multidlist)):
        if filled(multidlist[x], char):
            c2 = True
            break
    return c1 and c2

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
    print(grid)
    grid[position[0]][position[1]] = "X"
    for x in range(len(grid)):
        grid[x] = tuple(grid[x])
    grid = tuple(grid)
    if hasLinearChar(grid, "X"):
        print("X wins")
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
    if hasLinearChar(grid, "O"):
        print("O wins")
