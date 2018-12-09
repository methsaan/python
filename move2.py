#! /usr/bin/python3

import time
import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
rect = canvas.create_rectangle(30, 30, 90, 90, fill='red')
circ = canvas.create_oval(30, 30, 90, 90, fill='purple')
n = 0
size = 150
color = "red"
for x in range(1500):
    shape = [circ, rect]
    rand_shape = random.choice(shape)
    for x in range(4):
        canvas.move(rand_shape, 120, 0)
        tk.update()
        time.sleep(0.1)
    for x in range(4):
        canvas.move(rand_shape, 0, 120)
        tk.update()
        time.sleep(0.1)
    for x in range(4):
        canvas.move(rand_shape, -120, 0)
        tk.update()
        time.sleep(0.1)
    for x in range(4):
        canvas.move(rand_shape, 0, -120)
        tk.update()
        time.sleep(0.1)
    n = n + 1
    canvas.create_rectangle(180, 180, 420, 420, fill=color)
    canvas.create_text(300, 300, text=str(n), font=('helvetica', size))
    if n == 10:
        size = 125
        color = random.choice(["orange","blue","white","green","yellow"])
    if n == 15:
        size = 100
        color = random.choice(["orange","blue","white","green","yellow"])
    if n == 20:
        size = 75
        color = random.choice(["orange","blue","white","green","yellow"])
    if n == 25:
        size = 50
        color = random.choice(["orange","blue","white","green","yellow"])
    if n == 30:
        size = 25
        color = random.choice(["orange","blue","white","green","yellow"])
canvas.mainloop()
