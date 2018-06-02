#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600, bd=0, highlightthickness=0, bg="gray10")
canvas.pack()
canvas.create_rectangle(250, 200, 350, 400, fill="red")
canvas.create_rectangle(265, 260, 400, 300, fill="red")
canvas.create_rectangle(400, 260, 440, 300, fill="navajowhite")
canvas.create_line(420, 290, 440, 290)
canvas.create_line(420, 290, 440, 290)
canvas.create_line(420, 280, 440, 280)
canvas.create_line(420, 270, 440, 270)
face = canvas.create_rectangle(250, 100, 350, 200, fill="navajowhite")
canvas.create_rectangle(250, 400, 295, 550, fill="teal")
canvas.create_rectangle(305, 400, 350, 550, fill="teal")
hair1 = canvas.create_rectangle(230, 100, 250, 180, fill="black")
hair2 = canvas.create_rectangle(250, 80, 350, 100, fill="black")
hair3 = canvas.create_polygon(230, 180, 250, 200, 250, 180, fill="black")
tk.update()
time.sleep(2)
for x in range(60):
    canvas.move(face, -3, 0)
    canvas.move(hair1, -3, 0)
    canvas.move(hair2, -3, 0)
    canvas.move(hair3, -3, 0)
    tk.update()
    time.sleep(0.05)
tk.update()
newface = canvas.create_rectangle(70, 100, 170, 200, fill="white")
for x in range(114):
    canvas.move(face, 0, 3)
    canvas.move(newface, 0, 3)
    canvas.move(hair1, 0, 3)
    canvas.move(hair2, 0, 3)
    canvas.move(hair3, 0, 3)
    tk.update()
    time.sleep(0.01)
blues = ['gray80', 'gray76', 'gray72', 'gray68', 'gray64', 'gray60', 'gray56', 'gray52', 'gray48', 'gray44', 'gray40', 'gray36', 'gray32', 'gray28', 'gray24', 'gray20', 'gray16', 'gray12', 'gray11', 'gray10']
for x in blues:
    canvas.create_rectangle(70, 442, 170, 542, fill=x)
    tk.update()
    time.sleep(0.025)
canvas.create_line(100, 492, 100, 542, fill="red2")
canvas.create_line(100, 492, 90, 481, fill="red2")
tk.update()

canvas.mainloop()
