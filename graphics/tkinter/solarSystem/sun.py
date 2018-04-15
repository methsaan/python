#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1500, height=700)
canvas.pack()
def create_sun():
    canvas.create_oval(681, 281, 820, 420, fill="yellow")
canvas.mainloop()
