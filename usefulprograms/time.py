#! /usr/bin/python3

import random
import time
import datetime
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
while True:
    canvas.create_rectangle(0, 0, 700, 700, fill="springgreen", outline="springgreen")
    canvas.create_text(350, 350, fill="orange", text=str(datetime.datetime.now().time()), font=('helvetica', 60))
    tk.update()
canvas.mainloop()
