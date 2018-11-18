#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1100, height=800, bg="gray80")
canvas.pack()

xLabel = input("Enter a label for the x axis: ")
yLabel = input("Enter a label for the y axis: ")
canvas.create_text(550, 700, text=xLabel, font=("helvetica", 30), fill="black")
canvas.create_text(80, 400, text=yLabel, font=("helvetica", 20), fill="black")
canvas.create_line(250, 50, 250, 680, width=5)
canvas.create_line(250, 680, 1050, 680, width=5)
points = []
numOfData = int(input("How many " + str(yLabel) + "s are you going to record: "))
speed = 756/numOfData
progress = 250
for i in range(numOfData):
    points.append([0, int(input("Enter your next " + yLabel + ": "))])
points.append(points[len(points)-1])
for x in range(len(points)-1):
    canvas.create_oval(progress+speed-5, (800-points[x][1]-5)-120, progress+speed+5, (800-points[x][1]+5)-120, fill="red", outline="red")
    progress += speed
progress = 0
for y in points:
    canvas.create_line(progress+speed, 800-y[1]-120, progress+speed+speed, 800-points[y+1][1]+1-120, fill="red")
    progress += speed
def eventfunc(event):
    if event.char == "q":
        quit()
canvas.bind_all("<KeyPress-q>", eventfunc)
canvas.mainloop()
