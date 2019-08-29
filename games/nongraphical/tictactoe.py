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

grid = ((" ", " ", " "), (" ", " ", " "), (" ", " ", " "))
print("_________")
print("|  |  |  |")
print("|__|__|__|")
print("|  |  |  |")
print("|__|__|__|")
print("|  |  |  |")
print("|__|__|__|")
