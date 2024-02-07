#! /usr/bin/python3

import time
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=800, height=800)
canvas.pack()

rightSpeed = 15
leftSpeed = 15

left = canvas.create_oval(340, 90, 360, 110, fill="red")
right = canvas.create_oval(440, 90, 460, 110, fill="blue")

while True:
    def moveMotors(event):
        global rightSpeed
        global leftSpeed
        if event.keysym == 'Down':
            leftSpeed = -15
            rightSpeed = -15
        elif event.keysym == 'Left':
            if leftSpeed < 30:
                leftSpeed += 3
            rightSpeed = 0
        elif event.keysym == 'Right':
            if rightSpeed < 30:
                rightSpeed += 3
            leftSpeed = 0
        else:
            leftSpeed = 15
            rightSpeed = 15
    canvas.bind_all('<KeyPress-Left>', moveMotors)
    canvas.bind_all('<KeyPress-Right>', moveMotors)
    canvas.bind_all('<KeyPress-Down>', moveMotors)
    canvas.bind_all('<KeyPress-Up>', moveMotors)
    canvas.move(left, 0, leftSpeed)
    canvas.move(right, 0, rightSpeed)
    tk.update()
    time.sleep(0.5)

canvas.mainloop()
