#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_rectangle(0, 0, 800, 800, fill="black")
a = canvas.create_rectangle(0, 0, 100, 100, fill="red2")
b = canvas.create_rectangle(700, 100, 800, 200, fill="orange")
c = canvas.create_rectangle(0, 200, 100, 300, fill="yellow")
d = canvas.create_rectangle(700, 300, 800, 400, fill="springgreen")
e = canvas.create_rectangle(0, 400, 100, 500, fill="aqua")
f = canvas.create_rectangle(700, 500, 800, 600, fill="blue2")
g = canvas.create_rectangle(0, 600, 100, 700, fill="purple")
h = canvas.create_rectangle(700, 700, 800, 800, fill="deeppink")
colorlist = ['red', 'blue', 'green', 'gold']
def change(event):
    if event.keysym == 'Return':
        canvas.create_rectangle(0, 0, 800, 800, fill=random.choice(colorlist))
canvas.bind_all('<KeyPress-Return>', change)
for x in range(20):
    for x in range(25):
        a = canvas.create_rectangle(0, 0, 100, 100, fill="red2")             
        canvas.move(a, 28, 0)
        b = canvas.create_rectangle(700, 100, 800, 200, fill="orange")
        canvas.move(b, -28, 0)
        c = canvas.create_rectangle(0, 200, 100, 300, fill="yellow")
        canvas.move(c, 28, 0)
        d = canvas.create_rectangle(700, 300, 800, 400, fill="springgreen")
        canvas.move(d, -28, 0)
        e = canvas.create_rectangle(0, 400, 100, 500, fill="aqua")
        canvas.move(e, 28, 0)
        f = canvas.create_rectangle(700, 500, 800, 600, fill="blue2")
        canvas.move(f, -28, 0)
        g = canvas.create_rectangle(0, 600, 100, 700, fill="purple")
        canvas.move(g, 28, 0)
        h = canvas.create_rectangle(700, 700, 800, 800, fill="deeppink")
        canvas.move(h, -28, 0)
        colorlist = ['red', 'blue', 'green', 'gold']
        def write(ontext):
            canvas.create_text(400, 400, text=ontext, font=('helvetica', 40),  fill=random.choice(colorlist))
        write("HAPPY MOTHER'S DAY!")
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
        write("PRESS ENTER!")
        tk.update()
canvas.mainloop()
