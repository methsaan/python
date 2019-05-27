#! /usr/bin/python3

import random

sudokuBox = [[], [], [], []]

for x in range(4):
    for y in range(4):
        sudokuBox[x].append(random.randrange(1, 5))

for x in sudokuBox:
    print(x)
numToFind = int(input("Enter number to find: "))
numToFind = [x for x in sudokuBox if numToFind in x][0].index(numToFind)
print(numToFind)
row = (numToFind // 4)+1
column = 4 if numToFind%4 == 0 else numToFind % 4
if row < 3 and column < 3:
    box = 1
elif row >= 3 and column < 3:
    box = 3
elif row >= 3 and column >= 3:
    box = 4
else:
    box = 2
print("row:", row)
print("column:", column)
print("Box:", box)
