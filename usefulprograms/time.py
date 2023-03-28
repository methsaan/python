#! /usr/bin/python3

import random
import time
import datetime
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=950, height=950)
canvas.pack()
while True:
    #canvas.create_rectangle(0, 0, 950, 950, fill="blue", outline="blue")
    string = str(datetime.datetime.now().time())
    canvas.create_text(150, 472, fill="black", text=str(int(string[:-13])%12), font=("times", 150))
    canvas.create_text(156, 478, fill="red", text=str(int(string[:-13])%12), font=("times", 150))
    canvas.create_text(590, 472, fill="black", text=string[2:-7], font=("times", 150))
    canvas.create_text(596, 478, fill="red", text=string[2:-7], font=('times', 150))
    tk.update()
canvas.mainloop()
