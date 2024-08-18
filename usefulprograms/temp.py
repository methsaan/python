#! /usr/bin/python3

import random

'''
firstNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
secondNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]

combinations = []

for i in firstNum:
    for j in secondNum:
        combinations.append([i, j])

random.shuffle(combinations)

l = combinations[:30]

for x in range(len(l)):
    if x%3 == 0:
        print(x)
    print(l[x])
'''
firstNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]
secondNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]

combinations = []

for i in firstNum:
    for j in secondNum:
        combinations.append([i, j])

random.shuffle(combinations)

l = combinations[:30]

for x in range(len(l)):
    if x%3 == 0:
        print(x)
    print(l[x])
