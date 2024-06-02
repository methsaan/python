#! /usr/bin/python3

from tkinter import *
import random
import math
import time

WIDTH = 900
HEIGHT = 900

# Define quantities and units
forestWidthInPx = 4*WIDTH/5
forestHeightInPx = 4*HEIGHT/5
forestAreaInPx = forestWidthInPx * forestHeightInPx
hectaresInWidth = random.randrange(3, 5)
hectaresInHeight = hectaresInWidth
widthOfHectareInPx = forestWidthInPx/hectaresInWidth
heightOfHectareInPx = forestHeightInPx/hectaresInHeight
areaInHectares = hectaresInWidth * hectaresInHeight

# Meter is defined unrealistically big relative to hectare for visualization purposes
# Trees are measured in meter unit while land is measured in hectare units
metersInWidth = hectaresInWidth*3
metersInHeight = metersInWidth
widthOfMeterInPx = forestWidthInPx/metersInWidth
heightOfMeterInPx = widthOfMeterInPx

class Point3D:
    def __init__(self, x, y, z):
        # Set initial coordinates
        self.x = x # in and out
        self.y = y # left and right
        self.z = z # up and down
    def transform(self, pTransformVector):
        # Apply linear transformation on point given transformation matrix
        print(pTransformVector)

class Shape3D:
    def __init__(self, *points3d):
        # Set initial coordinates of shape vertices
        self.points = list(points3d)
    def transform(self, sTransformVector):
        # Transform all points given transformation matrix
        for point in self.points:
            point.transform(sTransformVector)

def vectorTransform(transformMatrix, vector):
    matrixProductx = round(transformMatrix[0][0]*vector[0] + transformMatrix[0][1]*vector[1] + transformMatrix[0][2]*vector[2], 4)
    matrixProducty = round(transformMatrix[1][0]*vector[0] + transformMatrix[1][1]*vector[1] + transformMatrix[1][2]*vector[2], 4)
    matrixProductz = round(transformMatrix[2][0]*vector[0] + transformMatrix[2][1]*vector[1] + transformMatrix[2][2]*vector[2], 4)
    matrixProduct = [matrixProductx, matrixProducty, matrixProductz]
    return matrixProduct

def multiplyTransformations(transformation1, transformation2):
    totalTransform = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(3):
        for y in range(3):
            totalTransform[x][y] = sum(transformation1[x][z] * transformation2[z][y] for z in range(3))
    return totalTransform

# Generate 3X3 linear transformation matrix
# given angles to rotate by
# +anglex = clockwise
# +angley = out of screen at top, into screen at bottom
# +anglez = towards -y at -x, towards +y at +x
def linTransformRotateVec(anglex, angley, anglez, v):
    # Initialize final vector
    transformedVector = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # transformation vector to rotate about x-axis
    xRotate = [[1, 0, 0], [0, math.cos(-math.radians(anglex)), -math.sin(-math.radians(anglex))], [0, math.sin(-math.radians(anglex)), math.cos(-math.radians(anglex))]]
    # transformation vector to rotate about y-axis
    yRotate = [[math.cos(-math.radians(angley)), 0, -math.sin(-math.radians(angley))], [0, 1, 0], [math.sin(-math.radians(angley)), 0, math.cos(-math.radians(angley))]]
    # transformation vector to rotate about z-axis
    zRotate = [[math.cos(-math.radians(anglez)), math.sin(-math.radians(anglez)), 0], [-math.sin(-math.radians(anglez)), math.cos(-math.radians(anglez)), 0], [0, 0, 1]]
    transformedVector = vectorTransform(xRotate, v)
    transformedVector = vectorTransform(yRotate, transformedVector)
    transformedVector = vectorTransform(zRotate, transformedVector)
    return transformedVector

# Return 2D coordinates of point on screen given 3D point
def point2D(point3D):
    print(point3D)

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

'''
# starting point
#origVector = [0, 8*math.sin(math.radians(140)), 8*math.cos(math.radians(140))]
#origVector = [8*math.sin(math.radians(150)), 0, 8*math.cos(math.radians(150))]
origVector = [8*math.cos(math.radians(20)), 8*math.sin(math.radians(20)), 0]
print(origVector)
for x in range(0, 361, 4):
    #origVector = vectorTransform(linTransformRotateVec(4, 0, 0), origVector)
    #origVector = vectorTransform(linTransformRotateVec(0, 4, 0), origVector)
    origVector = vectorTransform(linTransformRotateVec(0, 0, 4), origVector)
    print("Angle:", x, " Vector after rotating 4 degree:", origVector)
    #canvas.create_rectangle(origVector[1]*20+198, HEIGHT-(origVector[2]*20+198), origVector[1]*20+225, HEIGHT-(origVector[2]*20+225), fill="red")
    #canvas.create_rectangle(origVector[0]*20+198, HEIGHT-(origVector[2]*20+198), origVector[0]*20+225, HEIGHT-(origVector[2]*20+225), fill="red")
    canvas.create_rectangle(origVector[0]*20+198, HEIGHT-(origVector[1]*20+198), origVector[0]*20+225, HEIGHT-(origVector[1]*20+225), fill="red")
    tk.update()
    time.sleep(0.1)
'''

p = [0, 100, 0]
print(p)
p = linTransformRotateVec(45, 45, 45, p)
print(p)

canvas.mainloop()
