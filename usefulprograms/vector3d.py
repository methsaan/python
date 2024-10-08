#! /usr/bin/python3

from tkinter import *
import random
import math
import time

WIDTH = 900
HEIGHT = 900

# *Redefine

forestWidth = 20
forestHeight = 20


class Point3D:
    def __init__(self, x, y, z):
        # Set initial coordinates
        self.x = x # in and out
        self.y = y # left and right
        self.z = z # up and down
        self.v = [x, y, z]
    def rotate(self, xRot, yRot, zRot):
        # Apply linear transformation on point given transformation matrix
        tMatrix = linTransformRotateVec(xRot, yRot, zRot)
        self.v = vectorTransform(tMatrix, self.v)
        self.x = self.v[0]
        self.y = self.v[1]
        self.z = self.v[2]
    def translate(self, xMove, yMove, zMove):
        self.x += xMove
        self.y += yMove
        self.z += zMove
    def get2DCoords(self):
        xCoord = WIDTH/2 - self.x*(math.sqrt(WIDTH/2)/math.sqrt(2)) + self.y*math.sqrt(WIDTH/2)
        yCoord = HEIGHT/2 + self.x*(math.sqrt(HEIGHT/2)/math.sqrt(2)) - self.z*math.sqrt(HEIGHT/2)
        return xCoord, yCoord

class Shape3D:
    def __init__(self, *points3d, color, outlineWidth):
        # Set initial coordinates of shape vertices
        self.points = list(points3d)
        self.canvasObj = None
        self.color = color
        self.outlineWidth = outlineWidth
    def rotate(self, x, y, z):
        # Transform all points given transformation matrix
        for point in self.points:
            point.rotate(x, y, z)
    def translate(self, x, y, z):
        for point in self.points:
            point.translate(x, y, z)
    def updateCoords(self, c):
        coordsList = []
        for point in self.points:
            coordsList.append(list(point.get2DCoords()))
        if self.canvasObj == None:
            self.canvasObj = c.create_polygon(*sum(coordsList, []), fill=self.color, outline="black", width=self.outlineWidth)
            c.update()
        else:
            c.coords(self.canvasObj, *sum(coordsList, []))
            c.update()

class Icosahedron:
    def __init__(self, posx3d, posy3d, posz3d, sidelength, c):
        rectWidth = sidelength
        rectLength = math.sin((math.pi - math.acos(math.sqrt(5)/3))/2)*math.sqrt(3)*sidelength 
        self.rectxyCoords = [Point3D(posx3d+rectWidth/2, posy3d+rectLength/2, posz3d), Point3D(posx3d-rectWidth/2, posy3d+rectLength/2, posz3d), \
                       Point3D(posx3d-rectWidth/2, posy3d-rectLength/2, posz3d), Point3D(posx3d+rectWidth/2, posy3d-rectLength/2, posz3d)]
        self.rectyzCoords = [Point3D(posx3d, posy3d+rectWidth/2, posz3d+rectLength/2), Point3D(posx3d, posy3d-rectWidth/2, posz3d+rectLength/2), \
                       Point3D(posx3d, posy3d-rectWidth/2, posz3d-rectLength/2), Point3D(posx3d, posy3d+rectWidth/2, posz3d-rectLength/2)]
        self.rectxzCoords = [Point3D(posx3d+rectLength/2, posy3d, posz3d+rectWidth/2), Point3D(posx3d-rectLength/2, posy3d, posz3d+rectWidth/2), \
                             Point3D(posx3d-rectLength/2, posy3d, posz3d-rectWidth/2), Point3D(posx3d+rectLength/2, posy3d, posz3d-rectWidth/2)]
        self.rectangleCoords = [self.rectxyCoords, self.rectyzCoords, self.rectxzCoords]
        self.col = ["blue", "green", "orange", "purple", "red"]
        self.rectangles = [Shape3D(*self.rectangleCoords[i], color=self.col[i], outlineWidth=2) for i in range(len(self.rectangleCoords))]
        for rectangle in self.rectangles:
            rectangle.updateCoords(c)
    def rotate(self, x, y, z, c):
        for rectangle in self.rectangles:
            rectangle.rotate(x, y, z)
            rectangle.updateCoords(c)
    def translate(self, x, y, z, c):
        for rectangle in self.rectangles:
            rectangle.translate(x, y, z)
            rectangle.updateCoords(c)

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
# +anglex = counterclockwise
# +angley = into screen at top, out of screen at bottom
# +anglez = clockwise from overhead
def linTransformRotateVec(anglex, angley, anglez):
    # Initialize final vector
    transformedVector = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # transformation vector to rotate about x-axis
    xRotate = [[1, 0, 0], [0, math.cos(math.radians(anglex)), -math.sin(math.radians(anglex))], [0, math.sin(math.radians(anglex)), math.cos(math.radians(anglex))]]
    #print("xRotate:", xRotate)
    # transformation vector to rotate about y-axis
    yRotate = [[math.cos(math.radians(angley)), 0, -math.sin(math.radians(angley))], [0, 1, 0], [math.sin(math.radians(angley)), 0, math.cos(math.radians(angley))]]
    #print("yRotate:", yRotate)
    # transformation vector to rotate about z-axis
    zRotate = [[math.cos(math.radians(anglez)), math.sin(math.radians(anglez)), 0], [-math.sin(math.radians(anglez)), math.cos(math.radians(anglez)), 0], [0, 0, 1]]
    #print("zRotate:", zRotate)
    transformMatrix = multiplyTransformations(zRotate, yRotate)
    transformMatrix = multiplyTransformations(transformMatrix, xRotate)
    return transformMatrix

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_line(0, HEIGHT, WIDTH, 0, width=2)
canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, width=2)
canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, width=2)

for x in range(int(math.sqrt(WIDTH/2))):
    if x == int(math.sqrt(WIDTH/2)) - 1:
        canvas.create_line(WIDTH/2-x*math.sqrt(WIDTH/2), HEIGHT*(39/80), WIDTH/2-x*math.sqrt(WIDTH/2), HEIGHT*(41/80), width=2, fill="orange")
        canvas.create_line(WIDTH/2+x*math.sqrt(WIDTH/2), HEIGHT*(39/80), WIDTH/2+x*math.sqrt(WIDTH/2), HEIGHT*(41/80), width=2, fill="orange")
    else:
        canvas.create_line(WIDTH/2-x*math.sqrt(WIDTH/2), HEIGHT*(39/80), WIDTH/2-x*math.sqrt(WIDTH/2), HEIGHT*(41/80))
        canvas.create_line(WIDTH/2+x*math.sqrt(WIDTH/2), HEIGHT*(39/80), WIDTH/2+x*math.sqrt(WIDTH/2), HEIGHT*(41/80))
for x in range(int(math.sqrt(HEIGHT/2))):
    if x == int(math.sqrt(HEIGHT/2)) - 1:
        canvas.create_line(WIDTH*(39/80), HEIGHT/2+x*math.sqrt(HEIGHT/2),  WIDTH*(41/80), HEIGHT/2+x*math.sqrt(HEIGHT/2), width=2, fill="orange")
        canvas.create_line(WIDTH*(39/80), HEIGHT/2-x*math.sqrt(HEIGHT/2),  WIDTH*(41/80), HEIGHT/2-x*math.sqrt(HEIGHT/2), width=2, fill="orange")
    else:
        canvas.create_line(WIDTH*(39/80), HEIGHT/2+x*math.sqrt(HEIGHT/2),  WIDTH*(41/80), HEIGHT/2+x*math.sqrt(HEIGHT/2))
        canvas.create_line(WIDTH*(39/80), HEIGHT/2-x*math.sqrt(HEIGHT/2),  WIDTH*(41/80), HEIGHT/2-x*math.sqrt(HEIGHT/2))
for x in range(int(math.sqrt(HEIGHT))):
    canvas.create_line(WIDTH*(39/80)-x*(math.sqrt(WIDTH/2)/math.sqrt(2)), HEIGHT/2+x*(math.sqrt(HEIGHT/2)/math.sqrt(2)), WIDTH*(41/80)-x*(math.sqrt(WIDTH/2)/math.sqrt(2)), HEIGHT/2+x*(math.sqrt(HEIGHT/2)/math.sqrt(2)))
    canvas.create_line(WIDTH*(39/80)+x*(math.sqrt(WIDTH/2)/math.sqrt(2)), HEIGHT/2-x*(math.sqrt(HEIGHT/2)/math.sqrt(2)), WIDTH*(41/80)+x*(math.sqrt(WIDTH/2)/math.sqrt(2)), HEIGHT/2-x*(math.sqrt(HEIGHT/2)/math.sqrt(2)))

icos1 = Icosahedron(0, 5, 0, 10, canvas)

for i in range(3600):
    icos1.rotate(10, 0, 0, canvas)
    time.sleep(0.2)

canvas.mainloop()
