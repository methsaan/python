#! /usr/bin/python3

from tkinter import *
import random

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

# Generate 3X3 linear transformation matrix
# given angles to rotate by
def linTransformVec(anglex, angley, anglez):
    print(anglex, angley, anglez)

# Return 2D coordinates of point on screen given 3D point
def point2D(point3D):
    print(point3D)

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

print("Test")

canvas.mainloop()
