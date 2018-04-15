#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
a = canvas.create_rectangle(0, 0, 100, 100, fill="red2")
b = canvas.create_rectangle(700, 100, 800, 200, fill="orange")
c = canvas.create_rectangle(0, 200, 100, 300, fill="yellow")
d = canvas.create_rectangle(700, 300, 800, 400, fill="springgreen")
e = canvas.create_rectangle(0, 400, 100, 500, fill="aqua")
f = canvas.create_rectangle(700, 500, 800, 600, fill="blue2")
g = canvas.create_rectangle(0, 600, 100, 700, fill="purple")
h = canvas.create_rectangle(700, 700, 800, 800, fill="deeppink")
for x in range(20):
    for x in range(175):
        canvas.move(a, 4, 0)
        canvas.move(b, -4, 0)
        canvas.move(c, 4, 0)
        canvas.move(d, -4, 0)
        canvas.move(e, 4, 0)
        canvas.move(f, -4, 0)
        canvas.move(g, 4, 0)
        canvas.move(h, -4, 0)
        colorlist = ['red', 'blue', 'green', 'gold']
        canvas.create_text(400, 400, text="Happy birthday to me", font=('helvetica', 40),  fill=random.choice(colorlist))
        tk.update()
    for x in range(175):
        canvas.move(a, -4, 0)
        canvas.move(b, 4, 0)
        canvas.move(c, -4, 0)
        canvas.move(d, 4, 0)
        canvas.move(e, -4, 0)
        canvas.move(e, 0, 0)
        canvas.move(f, 4, 0)
        canvas.move(g, -4, 0)
        canvas.move(h, 4, 0)
        tk.update()
canvas.mainloop()
