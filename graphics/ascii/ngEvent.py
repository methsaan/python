#! /usr/bin/python3

import subprocess as sp
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=0, height=0)
canvas.pack()

x = 0
for x in range(1000000000000000000000000000000000):
    x += 0
    sp.call("clear", shell=True)
    print(" " * x + "O")
    def moveO(event):
        if event.keysym == "Left":
            x = x + 1
        elif event.keysym == "Right":
            x = x - 1
    canvas.bind_all("<KeyPress-Left>", moveO)
    canvas.bind_all("<KeyPress-Right>", moveO)
    canvas.mainloop()
