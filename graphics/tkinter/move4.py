#! /usr/bin/python3

import time
import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
def rect_shape():
    rect = canvas.create_rectangle(30, 30, 90, 90, fill='red')
    return rect
def circ_shape():
    circ = canvas.create_oval(30, 30, 90, 90, fill='purple')
    return circ
n = 0
size = 150
color = "red"
for x in range(28900):
    rand_shape = random.choice([circ_shape(), rect_shape()])
    for x in range(4):
        canvas.move(rand_shape, 120, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(4):
        canvas.move(rand_shape, 0, 120)
        tk.update()
        time.sleep(0.05)
    for x in range(4):
        canvas.move(rand_shape, -120, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(4):
        canvas.move(rand_shape, 0, -120)
        tk.update()
        time.sleep(0.05)
    n = n + 1
    canvas.create_rectangle(180, 180, 420, 420, fill=color)
    canvas.create_text(300, 300, text=str(n), font=('helvetica', size))
    if n == 15:
        size = 130
        color = random.choice(["orangered","blue2","navajowhite","springgreen","aqua"])
    if n == 30:
        size = 110
        color = random.choice(["orangered","blue2","navajowhite","springgreen","aqua"])
    if n == 45:
        size = 90
        color = random.choice(["orangered","blue2","navajowhite","springgreen","aqua"])
    if n == 60:
        size = 70
        color = random.choice(["orangered","blue2","navajowhite","springgreen","aqua"])
    if n == 75:
        size = 50
        color = random.choice(["orangered","blue2","navajowhite","springgreen","aqua"])
canvas.mainloop()
