#! /usr/bin/python3

from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=600, height=1000)
canvas.pack()
cursor = canvas.create_rectangle(10, 10, 11, 100, outline="red")
def type(event):
mainloop()
