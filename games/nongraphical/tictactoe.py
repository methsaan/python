#! /usr/bin/python3

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

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
a = (2, 4, 2)
print(a)
a = (4, 2, 4)
print(a)
