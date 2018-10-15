#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
a = 0
for x in range(100):
    canvas.create_oval(a-50, a-50, a+50, a+50, fill="gray"+str(x))
canvas.mainloop()
