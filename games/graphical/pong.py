#! /usr/bin/python3

import subprocess as sp
import random
import time
import math
from tkinter import *
tk = Tk()
WIDTH = 900
HEIGHT = 900
tk.title("PONG")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
colors = [random.choice(["blue", "black", "orangered"]), random.choice(["springgreen", "gold", "tomato"]), random.choice(["brown", "darkgreen", "purple"])]
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=colors[0], outline=colors[0])
scoreboard = canvas.create_rectangle(WIDTH/2-140, HEIGHT/2-70, WIDTH/2+140, HEIGHT/2, fill=colors[1], outline=colors[1])
paddle = canvas.create_rectangle(300, HEIGHT-60, 500, HEIGHT-40, fill=colors[1], outline=colors[1])
paddle2 = canvas.create_rectangle(300, 40, 500, 60, fill=colors[1], outline=colors[1])
ball = canvas.create_oval((WIDTH/2)-15, (HEIGHT/2)-15, (WIDTH/2)+15, (WIDTH/2)+15, fill=colors[2], outline=colors[2])
x = random.randrange(-12, 12)
if x > -7 and x < 7:
    x = random.randrange(7, 12)
y = random.randrange(-10, 10)
if y > -6 and y < 6:
    y = random.randrange(-10, -6)
score = 0
score2 = 0
running = True
while running:
    canvas.move(ball, x, y)
    pos = canvas.coords(ball)
    pos2 = canvas.coords(paddle)
    pos3 = canvas.coords(paddle2)
    left_of_paddle = pos2[2]-150
    right_of_paddle = pos2[2]+50
    left_of_paddle2 = pos3[2]-150
    right_of_paddle2 = pos3[2]+50
    if pos[3] >= HEIGHT-65 or pos[1] < 65:
        y = -y
    if pos[2] >= WIDTH or pos[0] < 0:
        x = -x
    if pos[3] >= WIDTH-65:
        y = random.randrange(-16, -4)
    if pos[1] <= 65:
        y = random.randrange(4, 16)
    if pos[3] >= WIDTH-65 and (pos[2] > right_of_paddle or pos[2] < left_of_paddle):
        scoreboard = canvas.create_rectangle(WIDTH/2-140, HEIGHT/2-70, WIDTH/2+140, HEIGHT/2, fill=colors[1], outline=colors[1])
        score2 = score2 + 1
        canvas.create_text(WIDTH/2, HEIGHT/2-40, text="P2 score: "+str(score2), font=("helvetica", 35), fill=colors[2])
    if pos[1] <= 65 and (pos[2] > right_of_paddle2 or pos[2] < left_of_paddle2):
        scoreboard = canvas.create_rectangle(WIDTH/2-140, HEIGHT/2-70, WIDTH/2+140, HEIGHT/2, fill=colors[1], outline=colors[1])
        score = score + 1
        canvas.create_text(WIDTH/2, HEIGHT/2-40, text="P1 score: "+str(score), font=("helvetica", 35), fill=colors[2])
    if score2 == 40:
        scoreboard = canvas.create_rectangle(WIDTH/2-140, HEIGHT/2-70, WIDTH/2+140, HEIGHT/2, fill=colors[1], outline=colors[1])
        canvas.create_text(WIDTH/2, HEIGHT/2-40, text="Winner: P2", font=("helvetica", 40), fill=colors[2])
        break
    if score == 40:
        scoreboard = canvas.create_rectangle(WIDTH/2-140, HEIGHT/2-70, WIDTH/2+140, HEIGHT/2, fill=colors[1], outline=colors[1])
        canvas.create_text(WIDTH/2, HEIGHT/2-40, text="Winner: P1", font=("helvetica", 40), fill=colors[2])
        break
    tk.update()
    time.sleep(0.01)
    def move_paddle(event):
        if event.keysym == 'Left':
            canvas.move(paddle, -40, 0)
        elif event.keysym == 'Right':
            canvas.move(paddle, 40, 0)
        if event.char == 'a':
            canvas.move(paddle2, -40, 0)
        elif event.char == 'd':
            canvas.move(paddle2, 40, 0)
    canvas.bind_all('<KeyPress-Left>', move_paddle)
    canvas.bind_all('<KeyPress-Right>', move_paddle)
    canvas.bind_all('<KeyPress-a>', move_paddle)
    canvas.bind_all('<KeyPress-d>', move_paddle)
canvas.mainloop()
