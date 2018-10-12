#! /usr/bin/python3

import random
import time
import math
from tkinter import *
tk = Tk()
WIDTH = 450
HEIGHT = 450
tk.title("Tkinter bounce game")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
colors = [random.choice(["blue", "black", "orangered"]), random.choice(["springgreen", "gold", "tomato"]), random.choice(["white", "peachpuff", "navajowhite"])]
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=colors[0], outline=colors[0])
paddle = canvas.create_rectangle(400, HEIGHT-60, 500, HEIGHT-40, fill=colors[1], outline=colors[1])
ball = canvas.create_oval((WIDTH/2)-15, (HEIGHT/2)-15, (WIDTH/2)+15, (WIDTH/2)+15, fill=colors[2], outline=colors[2])
x = random.randrange(-14, 14)
if x > -7 and x < 7:
    x = random.randrange(7, 14)
y = random.randrange(-15, 15)
if y > -8 and y < 8:
    y = random.randrange(-15, -8)
t1 = None
t2 = None
while True:
    canvas.move(ball, x, y)
    pos = canvas.coords(ball)
    if pos[3] >= WIDTH-65 or pos[1] < 0:
        t1 = time.time()
        y = -y
        y = random.randrange(-15, 15)
        if pos[3] >= WIDTH-65:
            t2 = time.time()
            if t2-t1 > 3:
                pos[0] = WIDTH/2
                pos[1] = HEIGHT/2
                pos[2] = WIDTH/2
                pos[3] = HEIGHT/2
            x = random.randrange(-14, 0)
        if pos[1] < 0:
            t2 = time.time()
            if t2-t1 > 3:
                pos[0] = WIDTH/2
                pos[1] = HEIGHT/2
                pos[2] = WIDTH/2
                pos[3] = HEIGHT/2
            x = random.randrange(0, 14)
    if pos[2] >= HEIGHT or pos[0] < 0:
        t1 = time.time()
        x = -x
        x = random.randrange(-14, 14)
        if pos[2] >= HEIGHT:
            t2 = time.time()
            if t2-t1 > 3:
                pos[0] = WIDTH/2
                pos[1] = HEIGHT/2
                pos[2] = WIDTH/2
                pos[3] = HEIGHT/2
            y = random.randrange(0, 15)
        if pos[0] < 0:
            t2 = time.time()
            if t2-t1 > 3:
                pos[0] = WIDTH/2
                pos[1] = HEIGHT/2
                pos[2] = WIDTH/2
                pos[3] = HEIGHT/2
            y = random.randrange(-15, 0)
    tk.update()
    time.sleep(0.01)
    def move_paddle(event):
        if event.keysym == 'Left':
            canvas.move(paddle, -50, 0)
        elif event.keysym == 'Right':
            canvas.move(paddle, 50, 0)
    canvas.bind_all('<KeyPress-Left>', move_paddle)
    canvas.bind_all('<KeyPress-Right>', move_paddle)
canvas.mainloop()
