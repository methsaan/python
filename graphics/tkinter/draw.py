#! /usr/bin/python3

import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
at = [250, 250, "red"]
pen = canvas.create_oval(at[0]-10, at[1]-10, at[0]+10, at[0]+10, fill="black", outline="black")
def movePen(event):
    if event.keysym == "Up":
        canvas.move(pen, 0, -5)
        canvas.create_line(at[0], at[1], at[0], at[1]-5, fill=at[2])
        at[1] -= 5
    elif event.keysym == "Down":
        canvas.move(pen, 0, 5)
        canvas.create_line(at[0], at[1], at[0], at[1]+5, fill=at[2])
        at[1] += 5
    elif event.keysym == "Left":
        canvas.move(pen, -5, 0)
        canvas.create_line(at[0], at[1], at[0]-5, at[1], fill=at[2])
        at[0] -= 5
    elif event.keysym == "Right":
        canvas.move(pen, 5, 0)
        canvas.create_line(at[0], at[1], at[0]+5, at[1], fill=at[2])
        at[0] += 5
    elif event.keysym == "Return":
        at[2] = random.choice(["red", "orange", "darkgoldenrod", "springgreen", "aqua", "purple", "black", "blue", "gray", "green"])
    elif event.keysym == "space":
        at[2] = ""
canvas.bind_all("<KeyPress-Up>", movePen)
canvas.bind_all("<KeyPress-Down>", movePen)
canvas.bind_all("<KeyPress-Left>", movePen)
canvas.bind_all("<KeyPress-Right>", movePen)
canvas.bind_all("<KeyPress-Return>", movePen)
canvas.bind_all("<space>", movePen)
canvas.mainloop()
