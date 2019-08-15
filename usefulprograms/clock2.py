#! /usr/bin/python3

import datetime
import time
import math
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800, bg="tan3")
canvas.pack()

canvas.create_oval(100, 100, 700, 700, fill="gray65", outline="black", width=25)
numCoords = [["XII", 400, 150], ["I", 500, 200], ["II", 600, 300], ["III", 650, 400], ["IV", 600, 500], ["V", 500, 600], ["VI", 400, 650], ["VII", 300, 600], ["VIII", 200, 500], ["IX", 150, 400], ["X", 200, 300], ["XI", 300, 200]]
for x in numCoords:
    canvas.create_text(x[1], x[2], text=x[0], font=("times", 30))
tk.update()
secondHand = canvas.create_line(400, 400, 400, 100, width=5, fill="red")
minuteHand = canvas.create_line(400, 400, 400, 200, width=10)
hourHand = canvas.create_line(400, 400, 400, 300, width=15)
canvas.create_oval(100, 100, 700, 700, fill="", outline="black", width=25)
tk.update()
xCoordPath1 = (list(range(400, 700, 20)) + list(range(700, 400, -20)) + list(range(400, 100, -20)) + list(range(100, 400, 20)))*10
yCoordPath1 = (list(range(100, 400, 20)) + list(range(400, 700, 20)) + list(range(700, 400, -20)) + list(range(400, 100, -20)))*10
xCoordPath2 = (list(range(400, 600, 14)) + list(range(600, 400, -14)) + list(range(400, 200, -14)) + list(range(200, 400, 14)))*10
yCoordPath2 = (list(range(200, 400, 14)) + list(range(400, 600, 14)) + list(range(600, 400, -14)) + list(range(400, 200, -14)))*10
xCoordPath3 = (list(range(400, 500, 34)) + list(range(500, 400, -34)) + list(range(400, 300, -34)) + list(range(300, 400, 34)))*10
yCoordPath3 = (list(range(300, 400, 34)) + list(range(400, 500, 34)) + list(range(500, 400, -34)) + list(range(400, 300, -34)))*10
hoursPassed = datetime.datetime.now().hour
minutesPassed = datetime.datetime.now().minute
secondsPassed = datetime.datetime.now().second
hourMoved = False
minuteMoved = False
secondMoved = False
while True:
    for z in range(hoursPassed, len(xCoordPath3)):
        canvas.coords(hourHand, 400, 400, xCoordPath3[z], yCoordPath3[z])
        hourMoved = True
        for y in range(0 if secondMoved else minutesPassed, 60):
            canvas.coords(minuteHand, 400, 400, xCoordPath2[y], yCoordPath2[y])
            minuteMoved = True
            for x in range(0 if secondMoved else secondsPassed, 60):
                canvas.coords(secondHand, 400, 400, xCoordPath1[x], yCoordPath1[x])
                tk.update()
                time.sleep(1)
                secondMoved = True
canvas.mainloop()
