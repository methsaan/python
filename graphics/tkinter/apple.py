#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
def appledrop():
    canvas.create_oval(20, 0, 580, 240, fill="green")
    apple1 = canvas.create_oval(270, 100, 330, 200, fill="red", outline="black")
    apple2 = canvas.create_oval(310, 100, 370, 200, fill="red", outline="red")
    apple3 = canvas.create_line(320, 130, 320, 60, fill="brown", width=10)
    apple4 = canvas.create_oval(430, 100, 490, 200, fill="red", outline="black")
    apple5 = canvas.create_oval(470, 100, 530, 200, fill="red", outline="black")
    apple6 = canvas.create_line(480, 130, 480, 60, fill="brown", width=10)
    canvas.create_rectangle(250, 200, 350, 550, fill="brown")
    canvas.move(apple1, -180, 0)
    canvas.move(apple2, -180, 0)
    canvas.move(apple3, -180, 0)
    tk.update()
    time.sleep(0.05)
    tk.update()
    a = random.randrange(-10, 10)
    b = random.randrange(-10, 10)
    c = random.randrange(-10, 10)
    for x in range(19):
        canvas.move(apple1, a, 18)
        canvas.move(apple2, b, 18)
        canvas.move(apple3, c, 18)
        tk.update()
        time.sleep(0.01)
    time.sleep(0.7)
    for x in range(19):
        canvas.move(apple4, a, 18)
        canvas.move(apple5, b, 18)
        canvas.move(apple6, c, 18)
        tk.update()
        time.sleep(0.01)
        tk.update()
def justdoit(event):
    if event.keysym == 'Return':
        appledrop()
canvas.bind_all('<KeyPress-Return>', justdoit)
canvas.mainloop()
