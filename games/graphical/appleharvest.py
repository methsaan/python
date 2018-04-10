#! /usr/bin/python3

# Useful modules
import random
import time
import math
import subprocess as sp
from tkinter import *
# Constants
WIDTH = 1000
HEIGHT = 1000
# Useful objects
tk = Tk()
tk.title("Tkinter apple harvest game")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

def spacepong():
    point = 0
    miss = 0
    # black background
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="cyan")
    # sun
    canvas.create_oval(320, 470, 680, 830, fill="yellow", outline="yellow")
    # ball speed
    x = 6
    y = 10
    # define the direction of the meteor
    if x == 0:
        x = 6
    if x >= -12 and x <= -9:
        n = 490
    elif x >= -8 and x <= -5:
        n = 510
    elif x >= -4 and x <= -1:
        n = 530
    elif x >= 1 and x <= 4:
        n = 550
    elif x >= 5 and x <= 8:
        n = 570
    elif x >= 9 and x <= 12:
        n = 590
    # paddle and meteor objects
    paddle = canvas.create_oval(0, 980, 200, 1000, fill="tomato", outline='tomato')
    ball = canvas.create_oval((WIDTH/2)-30, (HEIGHT/2)-30, WIDTH/2, (HEIGHT/2)+30, fill="red", outline="red")
    ball2 = canvas.create_oval(WIDTH/2-10, (HEIGHT/2)-30, (WIDTH/2)+20, (HEIGHT/2)+30, fill="red", outline="red")
    running = True
    while running:
        # move the ball
        canvas.move(ball, x, y)
        canvas.move(ball2, x, y)
        pos = canvas.coords(ball)
        padpos = canvas.coords(paddle)
        xpaddle1 = padpos[0] - 50
        xpaddle2 = padpos[0] + 50
        # detect whether the ball hit the wall
        if pos[3] >= WIDTH or pos[1] < 0:
            y = -y
        if pos[2] >= HEIGHT or pos[0] < 0:
            x = -x
        tk.update()
        time.sleep(0.01)
        # moves the paddle depending on the user's key symbol
        def move_paddle(event):
            if event.keysym == 'Left':
                canvas.move(paddle, -50, 0)
                xpaddle1 -= 50
                xpaddle2 -= 50
            elif event.keysym == 'Right':
                canvas.move(paddle, 50, 0)
                xpaddle1 += 50
                ypaddle2 += 50
        canvas.bind_all('<KeyPress-Left>', move_paddle)
        canvas.bind_all('<KeyPress-Right>', move_paddle)
        if pos[3] == 980:
            if pos[0] > xpaddle1 and pos[0] < xpaddle2:
                point = point + 0.5
                canvas.create_rectangle(370, 370, 630, 430, fill="black")
                canvas.create_text(500, 400, text="score: " + str(int(point)), font=('helvetica', 30), fill="white")
                tk.update()
            else:
                canvas.create_rectangle(350, 350, 650, 450, fill="black")
                canvas.create_text(500, 400, text="score: " + str(point), font=('helvetica', 30), fill="red")
                miss += 0.5
                canvas.create_rectangle(370, 370, 630, 430, fill="black")
                canvas.create_text(500, 400, text="STRIKE " + str(miss), fill="red", font=('helvetica', 30))
                if miss == 3:
                    canvas.create_text(500, 250, text="GAME OVER", font=('roboto', 90), fill="red")
                    canvas.create_text(500, 700, text="Score: " + str(point), font=('helvetica', 70), fill="white")
                    sp.call('clear', shell=True)
canvas.create_text(500, 500, text="press enter to start", font=("times", 50))
def start(event):
    if event.keysym == 'Return':
        spacepong()
        sp.call('clear', shell=True)
canvas.bind_all('<KeyPress-Return>', start)
canvas.mainloop()
