#! /usr/bin/python3

import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=750, height=750, bg='orange')
canvas.pack()

while True:
	ball = canvas.create_oval(325, 325, 425, 425, fill="springgreen", outline="springgreen")
	def moveBall(event):
		if event.keysym == "Up":
			canvas.move(ball, 0, -50)
		if event.keysym == "Down":
			canvas.move(ball, 0, 50)
		if event.keysym == "Left":
			canvas.move(ball, -50, 0)
		if event.keysym == "Right":
			canvas.move(ball, 50, 0)
	canvas.bind_all('<KeyPress-Up>', moveBall)
	canvas.bind_all('<KeyPress-Down>', moveBall)
	canvas.bind_all('<KeyPress-Left>', moveBall)
	canvas.bind_all('<KeyPress-Right>', moveBall)
	
	canvas.mainloop()
