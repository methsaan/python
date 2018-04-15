#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
#def x(event):
while True:
    canvas.create_rectangle(0, 0, 700, 700, fill="red", outline="red")
    canvas.create_text(350, 350, text=str(time.asctime()), font=('helvetica', 30))
    tk.update()
#canvas.bind_all('<KeyPress-Up>', x)
canvas.mainloop()
