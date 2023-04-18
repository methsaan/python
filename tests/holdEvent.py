#! /usr/bin/python3

import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()

has_prev_key_release = None
holdCnt = 0

def mvt1(x):
    canvas.move(shape, x, 40)
    tk.update()
    
def mvt2(x):
    canvas.move(shape, x, -30)
    tk.update()

def mvt3(x):
    canvas.move(shape, x, 0)
    tk.update()

def mvt4(x):
    canvas.move(shape, x, -20)
    tk.update()

def mvt5(x):
    canvas.move(shape, x, -40)
    tk.update()

def mvt6(x):
    canvas.move(shape, x, -10)
    tk.update()

def mvt7(x):
    canvas.move(shape, x, 0)
    tk.update()

def mvt8(x):
    canvas.move(shape, x, 50)
    tk.update()

mvts = [mvt1, mvt2, mvt3, mvt4, mvt5, mvt6, mvt7, mvt8]

shape = canvas.create_rectangle(100, 100, 200, 200, fill="orange")

def on_key_release(event): # runs once key is let go
    global has_prev_key_release
    has_prev_key_release = None
    global holdCnt
    holdCnt = 0
    print(holdCnt, "*", repr(event.char))

def on_key_press(event): # runs when key is pressed
    global holdCnt
    holdCnt += 1
    print(holdCnt, "on_key_press", repr(event.char))

def on_key_release_repeat(event): # runs while key is held
    global has_prev_key_release
    has_prev_key_release = tk.after_idle(on_key_release, event)
    print(holdCnt, "-", repr(event.char))

def on_key_press_repeat(event): # runs while key is held
    global has_prev_key_release
    if has_prev_key_release:
        global holdCnt
        holdCnt += 1
        tk.after_cancel(has_prev_key_release)
        has_prev_key_release = None
        print(holdCnt, "on_key_press_repeat", repr(event.char))
        if holdCnt % 4 == 0:
            mvts[(holdCnt-1)//4%8](20)
    else:
        on_key_press(event)

canvas.bind("<KeyRelease-Up>", on_key_release_repeat)
canvas.bind("<KeyPress-Up>", on_key_press_repeat)

canvas.focus_set()

canvas.mainloop()
