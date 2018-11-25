#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg="aqua")
canvas = Canvas(tk, width=1100, height=800, bg="aqua")
canvas.pack()

xLabel = input("Enter a label for the x axis: ")
yLabel = input("Enter a label for the y axis: ")
canvas.create_text(550, 700, text=xLabel, font=("helvetica", 30), fill="black")
canvas.create_text(120, 400, text=yLabel, font=("helvetica", 20), fill="black")
canvas.create_line(250, 50, 250, 680, width=5)
canvas.create_line(250, 680, 1050, 680, width=5)
points = []
avgcoords = []
numOfData = int(input("How many " + str(yLabel) + " values are you going to record: "))
speed = 756/numOfData
progress = 250
for i in range(numOfData):
    points.append([0, float(input("Enter your next " + yLabel + " value: "))])
points.append(points[len(points)-1])
for x in range(len(points)-1):
    canvas.create_oval(progress+speed-5, (800-points[x][1]-5)-120, progress+speed+5, (800-points[x][1]+5)-120, fill="red", outline="red")
    progress += speed
progress = 0
avgcoords.append(250+progress+speed)
avgcoords.append(800-points[0][1]-120)
for y in range(len(points)-2):
    canvas.create_line(250+progress+speed, 800-points[y][1]-120, 250+progress+speed+speed, 800-points[y+1][1]+1-120, fill="red", width=3)
    average = 0
    for x in list(range(y+2)):
        average += points[x][1]
    average /= y+2
    avgcoords.append(250+progress+speed+speed)
    avgcoords.append(800-average-120)
    progress += speed
a = 0
while a < len(avgcoords)-2:
    canvas.create_line(avgcoords[a], avgcoords[a+1], avgcoords[a+2], avgcoords[a+3], fill="blue")
    a += 2
def eventfunc(event):
    if event.char == "q":
        quit()
canvas.bind_all("<KeyPress-q>", eventfunc)
canvas.mainloop()
