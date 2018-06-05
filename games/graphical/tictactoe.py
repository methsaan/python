#! /usr/bin/python3

import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=300, height=300, bg="gray75")
canvas.pack()
canvas.create_rectangle(0, 0, 300, 300, fill="", width=10)
canvas.create_line(100, 0, 100, 300, width=5)
canvas.create_line(200, 0, 200, 300, width=5)
canvas.create_line(0, 100, 300, 100, width=5)
canvas.create_line(0, 200, 300, 200, width=5)
verti = [50, 150, 250]
horiz = [50, 150, 250]
def xo(event):
	if event.char == "1":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="1", font=('helvetica', 50))	
	if event.char == "2":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="2", font=('helvetica', 50))
	if event.char == "3":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="3", font=('helvetica', 50))
	if event.char == "4":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="4", font=('helvetica', 50))
	if event.char == "5":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="5", font=('helvetica', 50))
	if event.char == "6":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="6", font=('helvetica', 50))
	if event.char == "7":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="7", font=('helvetica', 50))
	if event.char == "8":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="8", font=('helvetica', 50))
	if event.char == "9":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="9", font=('helvetica', 50))
	if event.char == "a":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="a", font=('helvetica', 50))
	if event.char == "b":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="b", font=('helvetica', 50))
	if event.char == "c":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="c", font=('helvetica', 50))
	if event.char == "d":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="d", font=('helvetica', 50))
	if event.char == "e":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="e", font=('helvetica', 50))
	if event.char == "f":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="f", font=('helvetica', 50))
	if event.char == "g":
		x = random.choice(horiz)
		y = random.choice(verti)
		canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
		canvas.create_text(x, y, text="g", font=('helvetica', 50))
canvas.bind_all('<KeyPress-1>', xo)
canvas.bind_all('<KeyPress-2>', xo)
canvas.bind_all('<KeyPress-3>', xo)
canvas.bind_all('<KeyPress-4>', xo)
canvas.bind_all('<KeyPress-5>', xo)
canvas.bind_all('<KeyPress-6>', xo)
canvas.bind_all('<KeyPress-7>', xo)
canvas.bind_all('<KeyPress-8>', xo)
canvas.bind_all('<KeyPress-9>', xo)
canvas.bind_all('<KeyPress-a>', xo)
canvas.bind_all('<KeyPress-b>', xo)
canvas.bind_all('<KeyPress-c>', xo)
canvas.bind_all('<KeyPress-d>', xo)
canvas.bind_all('<KeyPress-e>', xo)
canvas.bind_all('<KeyPress-f>', xo)
canvas.bind_all('<KeyPress-g>', xo)
canvas.mainloop()

