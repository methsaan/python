#! /usr/bin/python3

from tkinter import *
import time
import random
import subprocess

tk = Tk()
plotx1 = None
canvas = Canvas(tk, width=400, height=400, bg="white", bd=0, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(0, 0, 400, 400, width=3)
canvas.create_line(50, 0, 50, 400, width=2)
canvas.create_line(100, 0, 100, 400, width=2)
canvas.create_line(150, 0, 150, 400, width=2)
canvas.create_line(200, 0, 200, 400, width=2)
canvas.create_line(250, 0, 250, 400, width=2)
canvas.create_line(300, 0, 300, 400, width=2)
canvas.create_line(350, 0, 350, 400, width=2)
canvas.create_line(400, 0, 400, 400, width=2)
canvas.create_line(0, 50, 400, 50, width=2)
canvas.create_line(0, 100, 400, 100, width=2)
canvas.create_line(0, 150, 400, 150, width=2)
canvas.create_line(0, 200, 400, 200, width=2)
canvas.create_line(0, 250, 400, 250, width=2)
canvas.create_line(0, 300, 400, 300, width=2)
canvas.create_line(0, 350, 400, 350, width=2)
canvas.create_line(0, 400, 400, 400, width=2)
print("Welcome to the quadrilateral plotter. Type -1 for the coordinate x1 to quit.")
while True:
    color = input("Enter band color: ")
    plotx1 = float(input("Enter coordinate x1: ")) * 50
    ploty1 = 400-float(input("Enter coordinate y1: ")) * 50
    plotx2 = float(input("Enter coordinate x2: ")) * 50
    ploty2 = 400-float(input("Enter coordinate y2: ")) * 50
    plotx3 = float(input("Enter coordinate x3: ")) * 50
    ploty3 = 400-float(input("Enter coordinate y3: ")) * 50
    plotx4 = float(input("Enter coordinate x4: ")) * 50
    ploty4 = 400-float(input("Enter coordinate y4: ")) * 50
    canvas.create_polygon(plotx1, ploty1, plotx2, ploty2, plotx3, ploty3, plotx4, ploty4, fill="",outline=color, width=5)
    print("Next polygon... Type -1 for the coordinate x1 to quit.")
canvas.mainloop()
