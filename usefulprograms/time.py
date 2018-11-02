#! /usr/bin/python3

import random
import time
import datetime
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=950, height=950)
canvas.pack()
while True:
    canvas.create_rectangle(0, 0, 950, 950, fill="red", outline="red")
    string = str(datetime.datetime.now().time())
    canvas.create_text(470, 470, fill="black", text=string[:-7], font=("times", 200))
    canvas.create_text(480, 480, fill="blue", text=string[:-7], font=('times', 200))
    tk.update()
canvas.mainloop()
