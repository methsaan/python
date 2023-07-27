#! /usr/bin/python3

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=1080, height=600)
canvas.pack()

canvas.create_polygon(50, 50, 150, 50, 150, 150, 50, 150, fill="white", outline="green", width=5)
canvas.create_polygon(50, 150, 150, 150, 600, 600, fill="white", outline="green", width=5) # triangle
canvas.create_polygon(150, 150, 150, 50, 600, 600, fill="white", outline="green", width=5) # triangle

canvas.create_polygon(200, 50, 400, 50, 400, 200, 200, 200,  fill="white", outline="orange", width=5)
canvas.create_polygon(400, 200, 600, 600, 400, 50,  fill="white", outline="orange", width=5)# triangle
canvas.create_polygon(400, 200, 600, 600, 200, 200,  fill="white", outline="orange", width=5)# triangle

canvas.create_polygon(170, 170, 270, 170, 270, 300, 170, 300, fill="white", outline="brown", width=5)
canvas.create_polygon(170, 300, 600, 600, 270, 300, fill="white", outline="brown", width=5)
canvas.create_polygon(270, 300, 270, 170, 600, 600, fill="white", outline="brown", width=5)

canvas.create_polygon(100, 550, 180, 550, 180, 400, 100, 400, fill="white", outline="red", width=5)
canvas.create_polygon(180, 550, 600, 600, 180, 400, fill="white", outline="red", width=5) # triangle
canvas.create_polygon(180, 550, 600, 600, 100, 550, fill="white", outline="red", width=5) # triangle

canvas.create_polygon(0, 500, 60, 500, 60, 450, 0, 450, fill="white", outline="blue", width=5)
canvas.create_polygon(60, 500, 600, 600, 60, 450, fill="white", outline="blue", width=5)# triangle
canvas.create_polygon(60, 500, 600, 600, 0, 500, fill="white", outline="blue", width=5)# triangle

canvas.create_polygon(300, 500, 250, 500, 250, 550, 430, 550, 430, 430, 300, 430, fill="white", outline="purple", width=5)
canvas.create_polygon(430, 550, 430, 430, 600, 600, fill="white", outline="purple", width=5)
canvas.create_polygon(430, 550, 250, 550, 600, 600, fill="white", outline="purple", width=5)

canvas.create_polygon(700, 20, 600, 20, 600, 200, 700, 200, fill="white", outline="cyan", width=5)
canvas.create_polygon(700, 200, 600, 600, 600, 200, fill="white", outline="cyan", width=5)# triangle

canvas.create_polygon(900, 550, 1000, 550, 1000, 400, 900, 400, fill="white", outline="magenta", width=5) #rectangle on left
canvas.create_polygon(600, 600, 900, 550, 900, 400, fill="white", outline="magenta", width=5)# triangle
canvas.create_polygon(900, 550, 600, 600, 1000, 550, fill="white", outline="magenta", width=5)# triangle

canvas.create_polygon(900, 50, 800, 50, 800, 200, 900, 200, fill="white", outline="gray", width=5)
canvas.create_polygon(800, 50, 600, 600, 800, 200, fill="white", outline="gray", width=5)# triangle
canvas.create_polygon(600, 600, 800, 200, 900, 200, fill="white", outline="gray", width=5)# triangle

canvas.create_polygon(930, 100, 930, 250, 1050, 250, 1050, 100, fill="white", outline="teal", width=5)
canvas.create_polygon(930, 100, 600, 600, 930, 250, fill="white", outline="teal", width=5)# triangle
canvas.create_polygon(600, 600, 930, 250, 1050, 250, fill="white", outline="teal", width=5)# triangle

canvas.create_polygon(600, 600, 670, 470, 670, 390, fill="white", outline="pink", width=5)
canvas.create_polygon(790, 550, 600, 550, 600, 470, 670, 470, 670, 390, 790, 390, fill="white", outline="pink", width=5)
canvas.create_polygon(790, 550, 600, 600, 600, 550, fill="white", outline="pink", width=5)

canvas.mainloop()
