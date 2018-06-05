#! /usr/bin/python3

import time
import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
canvas.create_rectangle(0, 0, 600, 600, fill="black")
color = ['springgreen', 'aqua', 'deeppink', 'red', 'yellow', 'blue', 'gold']
poly = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[0])
poly2 = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[1])
poly3 = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[2])
poly4 = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[3])
poly5 = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[4])
poly6 = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[5])
poly7 = canvas.create_polygon(30, 110, 110, 110, 70, 30, fill=color[6])
n = 0
size = 150
color = "red"
for x in range(1500):
    shape = [poly, poly2, poly3, poly4, poly5, poly6, poly7]
    rand_shape = random.choice(shape)
    for x in range(16):
        canvas.move(rand_shape, 30, 0)
        tk.update()
        time.sleep(0.01)
    for x in range(16):
        canvas.move(rand_shape, 0, 30)
        tk.update()
        time.sleep(0.01)
    for x in range(16):
        canvas.move(rand_shape, -30, 0)
        tk.update()
        time.sleep(0.01)
    for x in range(16):
        canvas.move(rand_shape, 0, -30)
        tk.update()
        time.sleep(0.01)
    n = n + 1
    canvas.create_rectangle(185, 185, 415, 415, fill=color, outline=color)
    canvas.create_text(300, 300, text=str(n), font=('helvetica', size), fill="white")
    if n%1 == 0:
        color = random.choice(['springgreen', 'green2', 'aqua', 'darkslategray1', 'deeppink', 'red', 'cyan', 'seagreen1', 'magenta3', 'yellow', 'tomato', 'peachpuff', 'maroon'])
    if n == 99:
        size = 80
    if n == 199:
        size = 80    
    if n == 299:
        size = 80
    if n == 499:
        size = 80
    if n == 999:
        size = 65
canvas.mainloop()
