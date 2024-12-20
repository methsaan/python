#! /usr/bin/python3

import math
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()

road = canvas.create_rectangle(0, 100, 600, 200, fill="gray")

police = canvas.create_oval(400, 400, 500, 500, fill="blue")
car = canvas.create_oval(100, 100, 200, 200, fill="green")

carLocation = [150, 150]
policeLocation = [450, 450]
roadFrontLocation = [450, 150]
carToPolice = canvas.create_line(carLocation[0], carLocation[1], policeLocation[0], policeLocation[1], width=3)
roadToPolice = canvas.create_line(roadFrontLocation[0], roadFrontLocation[1], policeLocation[0], policeLocation[1], width=3)
roadToCar = canvas.create_line(roadFrontLocation[0], roadFrontLocation[1], carLocation[0], carLocation[1], width=3)
roadToCarDist = math.sqrt(abs(roadFrontLocation[0]-carLocation[0])**2 + abs(roadFrontLocation[1]-carLocation[1])**2)
roadToPoliceDist = math.sqrt(abs(roadFrontLocation[0]-policeLocation[0])**2 + abs(roadFrontLocation[1]-policeLocation[1])**2)
carToPoliceDist = math.sqrt(abs(carLocation[0]-policeLocation[0])**2 + abs(carLocation[1]-policeLocation[1])**2)


for x in range(20):
    canvas.move(car, 10, 0)
    carLocation[0] += 10
    canvas.coords(carToPolice, carLocation[0], carLocation[1], policeLocation[0], policeLocation[1])
    canvas.coords(roadToCar, roadFrontLocation[0], roadFrontLocation[1], carLocation[0], carLocation[1])
    canvas.create_rectangle(0, 0, 600, 100, fill="white")
    canvas.create_rectangle(0, 200, 200, 600, fill="white")
    prevRoadToCarDist = roadToCarDist
    prevRoadToPoliceDist = roadToPoliceDist
    prevCarToPoliceDist = carToPoliceDist
    roadToCarDist = math.sqrt(abs(roadFrontLocation[0]-carLocation[0])**2 + abs(roadFrontLocation[1]-carLocation[1])**2)
    roadToPoliceDist = math.sqrt(abs(roadFrontLocation[0]-policeLocation[0])**2 + abs(roadFrontLocation[1]-policeLocation[1])**2)
    carToPoliceDist = math.sqrt(abs(carLocation[0]-policeLocation[0])**2 + abs(carLocation[1]-policeLocation[1])**2)
    canvas.create_text(100, 50, text="c: " + str(roadToCarDist), font=("helvetica", 20))
    canvas.create_text(500, 50, text="dc/dt: " + str(abs(prevRoadToCarDist - roadToCarDist)/2), font=("helvetica", 20))
    canvas.create_text(525, 200, text="a: " + str(roadToPoliceDist), font=("helvetica", 20))
    canvas.create_text(525, 400, text="da/dt: " + str(abs(prevRoadToPoliceDist - roadToPoliceDist)/2), font=("helvetica", 20))
    canvas.create_text(250, 350, text="b: " + str(carToPoliceDist), font=("helvetica", 20))
    canvas.create_text(250, 550, text="db/dt: " + str(abs(prevCarToPoliceDist - carToPoliceDist)/2), font=("helvetica", 20))
    print("dc/dt =", (carToPoliceDist*(abs(prevCarToPoliceDist - carToPoliceDist)/2) / math.sqrt(carToPoliceDist**2 - roadToPoliceDist**2)))
    tk.update()
    time.sleep(2)

canvas.mainloop()
