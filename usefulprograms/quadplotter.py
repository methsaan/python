#! /usr/bin/python3

from tkinter import *
import time
import random
import subprocess

tk = Tk()
plotx1 = None
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
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
while True:
    print("Welcome to the quadrilateral plotter. Type -1 for the following input to quit")
    plotx1 = int(input("Enter first coordinate x: ")) * 50
    if plotx1 == -50:
        print("Quitting ...               ", end="", flush=True)
        time.sleep(1)
        print("[DONE]")
        quit()
    ploty1 = int(input("Enter first coordinate y: ")) * 50
    plotx2 = int(input("Enter second coordinate x: ")) * 50
    ploty2 = int(input("Enter second coordinate y: ")) * 50
    plotx3 = int(input("Enter third coordinate x: ")) * 50
    ploty3 = int(input("Enter third coordinate y: ")) * 50
    plotx4 = int(input("Enter fourth coordinate x: ")) * 50
    ploty4 = int(input("Enter fourth coordinate y: ")) * 50
    print("loading quadrilateral ...      ", end="", flush=True)
    time.sleep(1)
    print("[DONE]")
    canvas.create_polygon(plotx1, ploty1, plotx2, ploty2, plotx3, ploty3, plotx4, ploty4, fill="",outline="red", width=3)
canvas.mainloop()
