#! /usr/bin/python3

def isLinear(*nums):
    difference = 0
    differenceList = []
    for x in range(len(nums)-1):
        difference = abs(nums[x]-nums[x+1])
        differenceList.append(difference)

