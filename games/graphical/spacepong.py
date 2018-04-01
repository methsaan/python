#! /usr/bin/python3

# Useful modules
import random
import time
import math
from tkinter import *
# Constants
WIDTH = 1000
HEIGHT = 1000
# Useful objects
tk = Tk()
tk.title("Tkinter spacepong game")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

def spacepong():
    point = 0
    # black background
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black")
    # sun
    canvas.create_oval(350, 500, 650, 800, fill="orange", outline="darkorange")
    def star(color, size, minus, plus, a, b, border, col2):
        # random star
        spot = random.randrange(minus, plus)
        spot2 = random.randrange(minus, plus)
        canvas.create_oval(spot, spot2-a, spot+size, spot2+size-b, fill=color, outline=col2, width=border)
    # alien
    canvas.create_oval(100, 100, 200, 200, fill="green2", outline="darkgreen", width=7)
    canvas.create_oval(100, 200, 200, 400, fill="green2", outline="darkgreen", width=7)
    canvas.create_line(120, 170, 180, 170, fill="darkgreen", width=7)
    canvas.create_rectangle(130, 130, 145, 145, fill="darkgreen", width=0)
    canvas.create_rectangle(170, 130, 185, 145, fill="darkgreen", width=0)
    canvas.create_line(75, 75, 100, 140, fill="darkgreen", width=7)
    canvas.create_line(225, 75, 200, 140, fill="darkgreen", width=7)
    canvas.create_oval(65, 75, 95, 105, fill="green2", outline="darkgreen", width=3)
    canvas.create_oval(210, 70, 240, 100, fill="green2", outline="darkgreen", width=3)
    canvas.create_line(50, 250, 120, 250, fill="darkgreen", width=21)
    canvas.create_line(200, 250, 250, 250, fill="darkgreen", width=21)
    canvas.create_line(125, 400, 100, 540, fill="darkgreen", width=21)
    canvas.create_line(175, 400, 200, 540, fill="darkgreen", width=21)
    for x in range(1600):
        # creates the star
        star('white', random.randrange(1, 17), -10, 1600, 280, 280, 3, 'gray33')
    for x in range(300):
        # sunshine
        spotx = random.randrange(350, 650)
        spoty = random.randrange(500, 800)
        canvas.create_rectangle(spotx, spoty, spotx+random.randrange(-20, 20), spoty+random.randrange(-20, 20), fill="orangered", outline="orangered", width=2)
    # mercury
    canvas.create_oval(100, 800, 150, 850, fill="rosybrown4")
    # venus
    canvas.create_oval(800, 825, 900, 925, fill="orangered")
    # astronaut
    canvas.create_rectangle(625, 75, 725, 175, fill="gray90", width=4, outline="gray70")
    canvas.create_rectangle(645, 95, 705, 155, fill="tomato", outline="tomato")
    canvas.create_rectangle(650, 175, 750, 325, fill="gray90", width=4, outline="gray70")
    canvas.create_line(650, 175, 600, 275, fill="gray60", width=28)
    canvas.create_line(750, 175, 700, 275, fill="gray60", width=28)
    canvas.create_rectangle(650, 325, 700, 425, fill="gray60", outline="black", width=5)
    canvas.create_rectangle(700, 325, 750, 425, fill="gray60", outline="black", width=5)
    canvas.create_line(675, 400, 700, 550, fill="gray50", width=45)
    canvas.create_line(725, 400, 750, 550, fill="gray50", width=45)
    # ball speed
    x = 1
    y = 2
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
    paddle = canvas.create_rectangle(0, 980, 100, 1000, fill="skyblue", outline='blue2')
    earthtext = canvas.create_text(50, 990, fill="blue2", text="e a r t h", font=('helvetica', 15))
    fire = canvas.create_polygon(467, 500, 533, 500, n, 340, fill="orange", outline="darkorange")
    ball = canvas.create_oval((WIDTH/2)-30, (HEIGHT/2)-30, (WIDTH/2)+30, (HEIGHT/2)+30, fill="lightgoldenrod2", outline="peachpuff")
    while True:
        # move the ball
        canvas.move(ball, x, y)
        canvas.move(fire, x, y)
        pos = canvas.coords(ball)
        pos2 = canvas.coords(fire)
        padpos = canvas.coords(paddle)
        xpaddle1 = padpos[0] - 50
        xpaddle2 = padpos[0] + 50
        # detect whether the ball hit the wall
        if pos[3] >= WIDTH or pos2[1] < 0:
            y = -y
        if pos[2] >= HEIGHT or pos[0] < 0:
            x = -x
        tk.update()
        time.sleep(0.01)
        # moves the paddle depending on the user's key symbol
        def move_paddle(event):
            if event.keysym == 'Left':
                canvas.move(paddle, -100, 0)
                canvas.move(earthtext, -100, 0)
                xpaddle1 -= 100
                xpaddle2 -= 100
            elif event.keysym == 'Right':
                canvas.move(paddle, 100, 0)
                canvas.move(earthtext, 100, 0)
                xpaddle1 += 100
                ypaddle2 += 100
        canvas.bind_all('<KeyPress-Left>', move_paddle)
        canvas.bind_all('<KeyPress-Right>', move_paddle)
        if pos[3] == 980:
            if pos[0] > xpaddle1 and pos[0] < xpaddle2:
                point = point + 1
                print("point", point)
                print("xpaddle1", xpaddle1)
                print("xpaddle2", xpaddle2)
                print("pos[0]", pos[0])
                print("pos[2]", pos[2])
                canvas.create_rectangle(350, 350, 650, 450, fill="gray20")
                canvas.create_text(500, 400, text="score: " + str(int(point)), font=('helvetica', 40), fill="red")
                tk.update()
            else:
                canvas.create_rectangle(350, 350, 650, 450, fill="gray20")
                canvas.create_text(500, 400, text="score: " + str(point), font=('helvetica', 40), fill="red")
# calls the spacepong() function
spacepong()
canvas.mainloop()
