#! /usr/bin/python3

import datetime
import time
import math
import decimal
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800, bg="tan3")
canvas.pack()

canvas.create_oval(100, 100, 700, 700, fill="gray65", outline="black", width=25)
numCoords = [["XII", 400, 150], ["I", 500, 200], ["II", 600, 300], ["III", 650, 400], ["IV", 600, 500], ["V", 500, 600], ["VI", 400, 650], ["VII", 300, 600], ["VIII", 200, 500], ["IX", 150, 400], ["X", 200, 300], ["XI", 300, 200]]
for x in numCoords:
    canvas.create_text(x[1], x[2], text=x[0], font=("times", 30))

minuteHand = canvas.create_line(400, 400, 400, 180, width=5)
secondHand = canvas.create_line(400, 400, 400, 180, width=2, fill="red")

tk.update()
canvas.mainloop()
