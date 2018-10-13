#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
d = canvas.create_oval(700, 300, 800, 400, fill="springgreen")
e = canvas.create_oval(0, 400, 100, 500, fill="aqua")
k = canvas.create_oval(300, 0, 400, 100, fill="springgreen")
l = canvas.create_oval(400, 700, 500, 800, fill="aqua")
for x in range(20):
    for x in range(165):
        canvas.move(k, 0, 5)
        canvas.move(l, 0, -5)
        canvas.move(d, -5, 0)
        canvas.move(e, 5, 0)
        tk.update()
        time.sleep(0.01)
    for x in range(165):
        canvas.move(k, 0, -5)
        canvas.move(l, 0, 5)
        canvas.move(d, 5, 0)
        canvas.move(e, -5, 0)
        tk.update()
        time.sleep(0.001)
canvas.mainloop()
