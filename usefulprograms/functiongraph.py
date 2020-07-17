#! /usr/bin/python3

from math import *
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=1000, bg="lightblue", bd=0, highlightthickness=0)
canvas.pack()

def plot(x, y):
    xcoord = 500+x
    ycoord = 500-y
    canvas.create_oval(xcoord-1, ycoord-1, xcoord+1, ycoord+1, fill="red", outline="red")
while True:
    function = input("Enter a function to graph: ")
    canvas.delete("all")
    yaxis = canvas.create_line(500, 0, 500, 1000, width=5)
    xaxis = canvas.create_line(0, 500, 1000, 500, width=5)
    for x in range(-8000, 8000, 25):
        canvas.create_line(x, 0, x, 1000)
        canvas.create_line(0, x, 1000, x)
    tk.update()
    y = 1
    for x in range(-8000, 8000, 50):
        exec("from math import *;from random import *;" + function)
        plot(x/15, y/15)
        tk.update()
canvas.mainloop()
