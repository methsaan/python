#! /usr/bin/python3

from tkinter import *
from tkinter import ttk
import random

win = Tk()
win.geometry("800x800")

#def selectMode():
    # does nothing

def line():
    print()
    # allow user to select points, enter length and angle of next point, draw lines between points until user clicks line button
    # add to shapelist and change command back to selectmode

def circle():
    print()
    # allow user to select center point, enter radius, draw circle with given radius around center point
    # add to shapelist and change command back to selectmode

def erase():
    print()
    # allow user to click on lines and curves between intersection points, erase selected line/curve, continue until select button is clicked
    # add to shapelist and change command back to selectmode

def rectangle():
    print()
    # allow user to select point, enter width and height of rectangle, draw rectangle
    # add to shapelist and change command back to selectmode

canvas = Canvas(win, width=800, height=800)
canvas.pack()

lineButton = Button(canvas, text="|", command=line)
lineButton.pack()

circleButton = Button(canvas, text="O", command=circle)
circleButton.pack()

eraseButton = Button(canvas, text=" ____\n/_/__/", command=erase)
eraseButton.pack()

rectangleButton = Button(canvas, text="[]", command=rectangle)
rectangleButton.pack()

win.mainloop()
