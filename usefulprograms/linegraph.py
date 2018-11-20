#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg="gray80")
canvas.pack()

xLabel = input("Enter a label for the x axis: ")
yLabel = input("Enter a label for the y axis: ")

canvas.mainloop()
