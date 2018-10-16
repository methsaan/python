#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
a = -200
b = -200
for y in range(100):
    c = 0
    for x in range(100):
        canvas.create_oval(a, b, a+500, b+500, fill="gray"+str(c), outline="gray"+str(c))
        a = a + 0.7
        b = b + 0.7
        c = c + 1
canvas.mainloop()
