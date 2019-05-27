#! /usr/bin/python3

import math
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800, bg="peachpuff")
canvas.pack()

minuteCoords = [400, 400, 400, 150]
def rotate(points, angle, center):
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points
canvas.create_oval(100, 100, 700, 700, fill="white", outline="black", width=25)
minuteHand = canvas.create_line(400, 400, 400, 150, width=5)
newHand = rotate(minuteCoords, 45, (400, 400))
canvas.mainloop()
