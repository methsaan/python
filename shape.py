#! /usr/bin/python3

import math

def area(length):
    return length**2*6

def volume(length):
    return length**3

def circleVolume(radius, height=0):
    return (math.pi*radius**2)*height

def areaCircle(radius, height=0):
    return (math.pi*radius**2)*2 + 2*math.pi*radius*height

print("Cube area:", area(6))
print("Cube volume:", volume(6))
print("Circle volume:", circleVolume(3))
print("Circle area:", areaCircle(3))
