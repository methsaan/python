#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
secs = int(input("How long? "))
x = "springgreen"
running = True
while running:
    tk.update()
    timestr = str(secs)
    secs -= 1
    if secs <= 9:
        if secs <= 4:
            x = "red"
        else:
            x = "orangered"
    if secs < 0:
        running = False
    time.sleep(1)
    canvas.create_rectangle(0, 0, 700, 700, fill=x, outline=x)
    canvas.create_text(350, 350, text=timestr, font=('tahoma', 105), fill="white")
canvas.create_rectangle(0, 0, 700, 700, fill="black", outline="orange")
canvas.create_text(350, 350, text="Time's up", font=('tahoma', 105), fill="white")
canvas.mainloop()
