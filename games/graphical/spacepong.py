#! /usr/bin/python3

import random
import time
import math
from tkinter import *
tk = Tk()
WIDTH = 1000
HEIGHT = 1000
tk.title("Tkinter bounce game")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
colors = [random.choice(["red", "orangered", "yellow"]), random.choice(["springgreen", "aqua", "blue2"]), random.choice(["deeppink", "purple1", "violetred1"])]
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=colors[0], outline=colors[0])
paddle = canvas.create_rectangle(300, HEIGHT-65, 600, HEIGHT-35, fill=colors[1], outline=colors[1])
ball = canvas.create_oval((WIDTH/2)-30, (HEIGHT/2)-30, (WIDTH/2)+30, (WIDTH/2)+30, fill=colors[2], outline=colors[2])
x = random.randrange(-12, 12)
y = random.randrange(6, 12)
if x == 0:
    x = 6
while True:
    canvas.move(ball, x, y)
    pos = canvas.coords(ball)
    if pos[3] >= WIDTH-65 or pos[1] < 0:
        y = -y
    if pos[2] >= HEIGHT or pos[0] < 0:
        x = -x
    tk.update()
    time.sleep(0.01)
    def move_paddle(event):
        if event.keysym == 'Left':
            canvas.move(paddle, -25, 0)
        elif event.keysym == 'Right':
            canvas.move(paddle, 25, 0)
    pos2 = canvas.coords(paddle)
    if pos2[1] == pos[3]:
        break
    canvas.bind_all('<KeyPress-Left>', move_paddle)
    canvas.bind_all('<KeyPress-Right>', move_paddle)
canvas.mainloop()
