#! /usr/bin/python3

import random
import time
import math
from tkinter import *
tk = Tk()
WIDTH = 1000
HEIGHT = 1000
tk.title("Tkinter spacepong game")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

def spacepong():
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black")
    canvas.create_oval(-100, 600, 1100, 1400, fill="orange", outline="darkorange")
    def star(color, size, minus, plus, a, b, border, col2):
        spot = random.randrange(minus, plus)
        spot2 = random.randrange(minus, plus)
        canvas.create_oval(spot, spot2-a, spot+size, spot2+size-b, fill=color, outline=col2, width=border)
    for x in range(300):
        star('white', 15, -10, 940, 240, 240, 6, 'gray33')
    for x in range(800):
        spotx = random.randrange(-100, 1100)
        spoty = random.randrange(560, 1000)
        canvas.create_rectangle(spotx, spoty, spotx+random.randrange(-30, 30), spoty+random.randrange(-30, 30), fill="orangered", outline="orangered", width=2)
    x = random.randrange(-12, 12)
    y = random.randrange(11, 17)
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
    track = canvas.create_rectangle(0, 935, 1000, 965, fill="orange", outline="orange")
    paddle = canvas.create_rectangle(300, HEIGHT-65, 600, HEIGHT-35, fill='blue2', outline='blue2')
    earthtext = canvas.create_text(470, 950, fill="blue4", text="EARTH", font=('helvetica', 25))
    fire = canvas.create_polygon(467, 500, 533, 500, n, 340, fill="orange", outline="darkorange")
    ball = canvas.create_oval((WIDTH/2)-30, (HEIGHT/2)-30, (WIDTH/2)+30, (HEIGHT/2)+30, fill="lightgoldenrod2", outline="peachpuff")
    canvas.create_oval(100, 100, 200, 200, fill="green2", outline="white", width=7)
    canvas.create_oval(100, 200, 200, 400, fill="green2", outline="white", width=7)
    canvas.create_line(120, 170, 180, 170, fill="white", width=7)
    canvas.create_rectangle(130, 130, 135, 135, fill="white", width=0)
    canvas.create_rectangle(170, 130, 175, 135, fill="white", width=0)
    while True:
        canvas.move(ball, x, y)
        canvas.move(fire, x, y)
        pos = canvas.coords(ball)
        pos2 = canvas.coords(fire)
        pos3 = canvas.coords(paddle)
        if pos[3] >= WIDTH-65 or pos2[1] < 0:
            y = -y
        if pos[2] >= HEIGHT or pos[0] < 0:
            x = -x
        tk.update()
        time.sleep(0.01)
        def move_paddle(event):
            if event.keysym == 'Left':
                canvas.move(paddle, -35, 0)
                canvas.move(earthtext, -35, 0)
            elif event.keysym == 'Right':
                canvas.move(paddle, 35, 0)
                canvas.move(earthtext, 35, 0)
        canvas.bind_all('<KeyPress-Left>', move_paddle)
        canvas.bind_all('<KeyPress-Right>', move_paddle)
spacepong()
canvas.mainloop()
