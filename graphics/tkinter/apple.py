#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
canvas.create_oval(20, 0, 580, 240, fill="green")
apple1 = canvas.create_oval(270, 100, 330, 200, fill="red", outline="red")
apple2 = canvas.create_oval(310, 100, 370, 200, fill="red", outline="red")
apple3 = canvas.create_line(320, 130, 320, 60, fill="brown")
apples = [apple1, apple2, apple3]
canvas.create_rectangle(250, 200, 350, 550, fill="brown")
canvas.move(apple1, -180, 0)
canvas.move(apple2, -180, 0)
canvas.move(apple3, -180, 0)
tk.update()
time.sleep(0.05)
tk.update()
for x in range(19):
    canvas.move(apple1, 0, 18)
    canvas.move(apple2, 0, 18)
    canvas.move(apple3, 0, 18)
    tk.update()
    time.sleep(0.01)
time.sleep(0.7)
apple4 = canvas.create_oval(430, 100, 490, 200, fill="red", outline="red")
apple5 = canvas.create_oval(470, 100, 530, 200, fill="red", outline="red")
apple6 = canvas.create_line(480, 130, 480, 60, fill="brown")
apples2 = [apple4, apple5, apple5]
for x in range(19):
    canvas.move(apple4, 0, 18)
    canvas.move(apple5, 0, 18)
    canvas.move(apple6, 0, 18)
    tk.update()
    time.sleep(0.01)
    tk.update()
canvas.mainloop()
