#! /usr/bin/python3

def isSubset(l, subset):
    result = True
    for x in subset:
        if x not in l:
            result = False
    return result

numOfSameConstraints = int(input())

sameConstraints = []

for x in range(numOfSameConstraints):
    sameConstraints.append(input().split())

numOfDiffConstraints = int(input())

diffConstraints = []

for x in range(numOfDiffConstraints):
    diffConstraints.append(input().split())

numOfTestGroups = int(input())

testGroups = []

for x in range(numOfTestGroups):
    testGroups.append(input().split())

constraintsViolated = 0

for x in testGroups:
    for y in sameConstraints:
        if isSubset(x, y):
            print(x, " -xxx-", y)
        else:
            print(x, " -vvv-", y)
