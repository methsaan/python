#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
a = canvas.create_oval(700, 100, 800, 200, fill="red")
b = canvas.create_oval(0, 600, 100, 700, fill="blue")
c = canvas.create_oval(100, 0, 200, 100, fill="red")
d = canvas.create_oval(600, 700, 700, 800, fill="blue")
for x in range(20):
    for x in range(70):
        canvas.move(b, 0, 10)
        canvas.move(c, 0, -10)
        canvas.move(d, -10, 0)
        canvas.move(a, 10, 0)
        tk.update()
    for x in range(175):
        canvas.move(b, 0, -10)
        canvas.move(c, 0, 10)
        canvas.move(d, 10, 0)
        canvas.move(a, -10, 0)
        tk.update()
canvas.mainloop()
