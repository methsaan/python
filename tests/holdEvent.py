#! /usr/bin/python3

import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()

has_prev_key_release = None

shape = canvas.create_rectangle(100, 100, 200, 200, fill="orange")

def on_key_release(event): # runs once key is let go
    global has_prev_key_release
    has_prev_key_release = None
    print("*", repr(event.char))

def on_key_press(event): # runs when key is pressed
    print("on_key_press", repr(event.char))
    canvas.move(shape, 10, 0)
    #tk.update()
    #time.sleep(2)

def on_key_release_repeat(event): # runs while key is held
    global has_prev_key_release
    has_prev_key_release = tk.after_idle(on_key_release, event)
    print("-", repr(event.char))

def on_key_press_repeat(event): # runs while key is held
    global has_prev_key_release
    if has_prev_key_release:
        tk.after_cancel(has_prev_key_release)
        has_prev_key_release = None
        print("on_key_press_repeat", repr(event.char))
        canvas.move(shape, 10, 0)
        #tk.update()
        #time.sleep(2)
    else:
        on_key_press(event)

canvas.bind("<KeyRelease-a>", on_key_release_repeat)
canvas.bind("<KeyPress-a>", on_key_press_repeat)

canvas.bind("<KeyRelease-s>", on_key_release_repeat)
canvas.bind("<KeyPress-s>", on_key_press_repeat)
canvas.focus_set()

canvas.mainloop()
