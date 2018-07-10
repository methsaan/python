#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
while True:
    canvas.create_rectangle(0, 0, 700, 700, fill="lightblue", outline="lightblue")
    canvas.create_text(350, 350, text=str(time.asctime()), font=('helvetica', 46))
    tk.update()
canvas.mainloop()
