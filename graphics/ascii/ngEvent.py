#! /usr/bin/python3

import subprocess as sp
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=100, height=100)

x = 0
while True:
    sp.call('clear', shell=True)
    print((" " * x) + "O")
    def moveO(event):
        if event.keysym == "Up":
            x++
        elif event.keysym == "down":
            x--
    canvas.bind_all("<KeyPress-Up>")
    canvas.bind_all("<KeyPress-Down>")

