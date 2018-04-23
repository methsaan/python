#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
def clear():
    canvas.create_rectangle(0, 0, 600, 600, fill="black")
def hand(x):
    clear()
    canvas.create_rectangle(200, 200, 450, 450, fill="orangered", outline="orangered")
    canvas.create_rectangle(200, 50, 250, 200, fill="orangered", outline="orangered")
    canvas.create_rectangle(300, 50, 350, 200, fill="orangered", outline="orangered")
    canvas.create_rectangle(400, 50, 450, 200, fill="orangered", outline="orangered")
    canvas.create_rectangle(450, 300, 560, 350, fill="orangered", outline="orangered")
    tk.update()
    if x == True:
        time.sleep(6)
def blink():
    for x in range(6):
        hand(False)
        tk.update()
        time.sleep(0.5)
        x = True
        clear()
        tk.update()
        time.sleep(0.5)
def man(y):
    canvas.create_rectangle(250, 200, 350, 400, fill="springgreen", outline="springgreen")
    canvas.create_rectangle(230, 60, 370, 200, fill="springgreen", outline="springgreen")
    canvas.create_line(340, 350, 260, 230, fill="springgreen3", width=30)
    canvas.create_line(340, 230, 450, 350, fill="springgreen3", width=30)
    canvas.create_line(260, 390, 150, 500, fill="springgreen3", width=20)
    canvas.create_line(340, 390, 300, 500, fill="springgreen3", width=20)
    tk.update()
    if y == True:
        time.sleep(3)
def manblink():
    for x in range(6):
        man(False)
        tk.update()
        time.sleep(0.5)
        y = True
        clear()
        tk.update()
        time.sleep(0.5)
while True:
    hand(True)
    tk.update()
    blink()
    tk.update()
    man(True)
    tk.update()
    blink()
    tk.update()
canvas.mainloop()
