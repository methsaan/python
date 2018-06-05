#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=300, height=300, bg="gray75")
canvas.pack()
canvas.create_rectangle(0, 0, 300, 300, fill="", width=10)
canvas.create_line(100, 0, 100, 300, width=5)
canvas.create_line(200, 0, 200, 300, width=5)
canvas.create_line(0, 100, 300, 100, width=5)
canvas.create_line(0, 200, 300, 200, width=5)
def xo(event):
	if event.char == "a":
		canvas.create_text(150, 150, text="1", font=('helvetica', 50))
	elif event.char == "b":
		canvas.create_text(150, 150, text="2", font=('helvetica', 50))
canvas.bind_all('<KeyPress-Shift_L>', xo)
canvas.bind_all('<KeyPress-Control_L>', xo)
canvas.mainloop()
