#! /usr/bin/python2

width1 = int(input("Enter width of matrix 1: "))
height1 = int(input("Enter width of matrix 1: "))
operator = input("Enter operator: ")
matrix1 = []
for x in range(height1):
    matrix1.append([])
if operator == "x":
    height2 = width1
    width2 = height1
else:
    height2 = height1
    width2 = height2
matrix2 = []
for x in range(height2):
    matrix2.append([])
for x in range(len(matrix1)):

