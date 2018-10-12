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
x = random.randrange(-28, 28)
if x > -14 and x < 14:
    x = random.randrange(14, 28)
y = random.randrange(-30, 30)
if y > -15 and y < 15:
    y = random.randrange(-30, -15)
while True:
    canvas.move(ball, x, y)
    pos = canvas.coords(ball)
    cnt = 0
    #for x in pos:
     #   print(str(cnt) + ": " + str(x))
      #  cnt = cnt + 1
    if pos[3] >= WIDTH-65 or pos[1] < 0:
        y = -y
        pos = canvas.coords(ball)
        if pos[3] < WIDTH-65 or pos[1] < 0:
            if y > 0:
                y = random.randrange(10, 28)
            elif y < 0:
                y = random.randrange(-28, -10)
            else:
                print("", end="", flush=True)
    if pos[2] >= HEIGHT or pos[0] < 0:
        x = -x
        pos = canvas.coords(ball)
        if pos[2] > HEIGHT or pos[0] < 0:
            if x > 0:
               x = random.randrange(10, 30)
            elif x < 0:
               x = random.randrange(-30, -10)
            else:
               print("", end="", flush=True)
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
