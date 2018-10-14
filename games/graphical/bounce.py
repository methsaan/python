#! /usr/bin/python3

import subprocess as sp
import random
import time
import math
from tkinter import *
tk = Tk()
WIDTH = 475
HEIGHT = 475
tk.title("EXTREMELY HARD!")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
colors = [random.choice(["blue", "black", "orangered"]), random.choice(["springgreen", "gold", "tomato"]), random.choice(["white", "peachpuff", "navajowhite"])]
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=colors[0], outline=colors[0])
scoreboard = canvas.create_rectangle(WIDTH/2-70, HEIGHT/2-50, WIDTH/2+70, HEIGHT/2-20, fill=colors[1], outline=colors[1])
paddle = canvas.create_rectangle(400, HEIGHT-60, 500, HEIGHT-40, fill=colors[1], outline=colors[1])
ball = canvas.create_oval((WIDTH/2)-15, (HEIGHT/2)-15, (WIDTH/2)+15, (WIDTH/2)+15, fill=colors[2], outline=colors[2])
x = random.randrange(-10, 10)
if x > -5 and x < 5:
    x = random.randrange(5, 10)
y = random.randrange(-12, 12)
if y > -6 and y < 6:
    y = random.randrange(-12, -6)
score = 0
strike = 0
running = True
while running:
    canvas.move(ball, x, y)
    pos = canvas.coords(ball)
    pos2 = canvas.coords(paddle)
    left_of_paddle = pos2[2]-50
    right_of_paddle = pos2[2]+50
    if pos[3] >= WIDTH-65 or pos[1] < 0:
        y = -y
    if pos[2] >= HEIGHT or pos[0] < 0:
        x = -x
    if pos[3] >= WIDTH-65:
        y = random.randrange(-12, -2)
    if pos[3] >= WIDTH-65 and (pos[2] < right_of_paddle and pos[2] > left_of_paddle):
        scoreboard = canvas.create_rectangle(WIDTH/2-70, HEIGHT/2-50, WIDTH/2+70, HEIGHT/2-20, fill=colors[1], outline=colors[1])
        score = score + 1
        canvas.create_text(WIDTH/2, HEIGHT/2-40, text="score: "+str(score), font=("helvetica", 20), fill=colors[2])
    if pos[3] >= WIDTH-65 and (pos[2] > right_of_paddle or pos[2] < left_of_paddle):
        scoreboard = canvas.create_rectangle(WIDTH/2-70, HEIGHT/2-50, WIDTH/2+70, HEIGHT/2-20, fill=colors[1], outline=colors[1])
        strike = strike + 1
        canvas.create_text(WIDTH/2, HEIGHT/2-40, text="strikes: "+str(strike), font=("helvetica", 20), fill=colors[2])
        if strike == 30:
            sp.call("clear", shell=True)
            print("GAME OVER\nScore: ", score)
            break
    tk.update()
    time.sleep(0.01)
    def move_paddle(event):
        if event.keysym == 'Left':
            canvas.move(paddle, -40, 0)
        elif event.keysym == 'Right':
            canvas.move(paddle, 40, 0)
    canvas.bind_all('<KeyPress-Left>', move_paddle)
    canvas.bind_all('<KeyPress-Right>', move_paddle)
canvas.mainloop()
