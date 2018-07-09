#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
color = "red"
at = [250, 250]
pen = canvas.create_oval(at[0]-10, at[1]-10, at[0]+10, at[0]+10, fill=color)
def movePen(event):
    temp = at
    if event.keysym == "Up":
        canvas.move(pen, 0, -40)
        at[1] += 40
        canvas.create_line(temp[0], temp[1], at[0], at[1], fill="red")
    elif event.keysym == "Down":
        canvas.move(pen, 0, 40)
        at[1] -= 40
        canvas.create_line(temp[0], temp[1], at[0], at[1], fill="red")
    elif event.keysym == "Left":
        canvas.move(pen, -40, 0)
        at[0] -= 40
        canvas.create_line(temp[0], temp[1], at[0], at[1], fill="red")
    elif event.keysym == "Right":
        canvas.move(pen, 40, 0)
        at[0] += 40
        canvas.create_line(temp[0], temp[1], at[0], at[1], fill="red")
canvas.bind_all("<KeyPress-Up")
canvas.bind_all("<KeyPress-Down")
canvas.bind_all("<KeyPress-Left")
canvas.bind_all("<KeyPress-Right")
canvas.mainloop()
