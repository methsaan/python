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
	input_ = event.char
	x = random.choice(horiz)
	y = random.choice(verti)
	canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="gray75")
	canvas.create_text(x, y, text=event.char, font=('helvetica', 50))
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

