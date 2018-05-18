#! /usr/bin/python3

from tkinter import *
import time
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_line(50, 0, 50, 400)
canvas.create_line(100, 0, 100, 400)
canvas.create_line(150, 0, 150, 400)
canvas.create_line(200, 0, 200, 400)
canvas.create_line(250, 0, 250, 400)
canvas.create_line(300, 0, 300, 400)
canvas.create_line(350, 0, 350, 400)
canvas.create_line(400, 0, 400, 400)
canvas.create_line(0, 50, 400, 50)
canvas.create_line(0, 100, 400, 100)
canvas.create_line(0, 150, 400, 150)
canvas.create_line(0, 200, 400, 200)
canvas.create_line(0, 250, 400, 250)
canvas.create_line(0, 300, 400, 300)
canvas.create_line(0, 350, 400, 350)
canvas.create_line(0, 400, 400, 400)

canvas.mainloop()
