#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
secs = 0
mins = 0
hrs = 0
def printTime(s, m, h):
    canvas.create_rectangle(0, 0, 700, 700, fill="springgreen")
    if h < 10:
        canvas.create_text(250, 350, text="0" + str(h), font=("helvetica", 40))
    else:
        canvas.create_text(250, 350, text=str(h))
    canvas.create_text(300, 350, text=": ", font=("helvetica", 40))
    if m < 10:
        canvas.create_text(350, 350, text="0" + str(m), font=("helvetica", 40))
    else:
        canvas.create_text(350, 350, text=str(m))
    canvas.create_text(400, 350, text=": ", font=("helvetica", 40))
    if s < 10:
        canvas.create_text(450, 350, text="0" + str(s), font=("helvetica", 40))
    else:
        canvas.create_text(450, 350, text=str(s), font=("helvetica", 40))
    tk.update()
while True:
    printTime(secs, mins, hrs)
    time.sleep(1)
    secs = secs + 1
    if secs == 60:
        secs = 0
        mins = mins + 1
    if mins == 60:
        mins = 0
        hrs = hrs + 1
    tk.update()
canvas.mainloop()
