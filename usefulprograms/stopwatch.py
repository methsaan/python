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
secs2 = "0" + str(secs)
mins2 = "0" + str(mins)
hrs2 = "0" + str(hrs)
while True:
    timestr = str(" " + str(hrs) + ":" + " " + str(mins) + ":" + " " + str(secs))
    secs += 1
    if secs == 60:
        mins += 1
        secs = 0
    if mins == 60:
        hrs += 1
        mins = 0
    time.sleep(0.9)
    canvas.create_rectangle(0, 0, 700, 700, fill="springgreen", outline="aqua")
    canvas.create_text(350, 350, text=timestr, font=('helvetica', 45))
    tk.update()
canvas.mainloop()
