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

canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black")
canvas.create_oval(100, 600, 900, 1400, fill="orange")
def star(color, size, minus, plus):
    spot = random.randrange(minus, plus)
    spot2 = random.randrange(minus, plus)
    canvas.create_oval(spot, spot2, spot+size, spot2+size, fill=color, outline="gray50")
for x in range(300):
    star('white', 15, -10, 940)
paddle = canvas.create_rectangle(300, HEIGHT-65, 600, HEIGHT-35, fill='blue2', outline='blue2')
earthtext = canvas.create_text(470, 950, fill="chartreuse2", text="EARTH", font=('helvetica', 25))
fire = canvas.create_polygon(467, 500, 533, 500, 500, 390, fill="orange", outline="red")
ball = canvas.create_oval((WIDTH/2)-30, (HEIGHT/2)-30, (WIDTH/2)+30, (HEIGHT/2)+30, fill="peachpuff", outline="peachpuff")
x = random.randrange(-12, 12)
y = random.randrange(9, 15)
if x == 0:
    x = 6
while True:
    canvas.move(ball, x, y)
    canvas.move(fire, x, y)
    pos = canvas.coords(ball)
    pos2 = canvas.coords(fire)
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
canvas.mainloop()
