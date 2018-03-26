#! /usr/bin/python3

from tkinter import *
tk = Tk()
tk.title("Events and bindings")
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_line(100, 0, 100, 800)
canvas.create_line(200, 0, 200, 800)
canvas.create_line(300, 0, 300, 800)
canvas.create_line(400, 0, 400, 800)
canvas.create_line(500, 0, 500, 800)
canvas.create_line(600, 0, 600, 800)
canvas.create_line(700, 0, 700, 800)
canvas.create_line(0, 100, 800, 100)
canvas.create_line(0, 200, 800, 200)
canvas.create_line(0, 300, 800, 300)
canvas.create_line(0, 400, 800, 400)
canvas.create_line(0, 500, 800, 500)
canvas.create_line(0, 600, 800, 600)
canvas.create_line(0, 700, 800, 700)
a = 0
b = 0
c = 200
d = 200
cursor = canvas.create_rectangle(a, b, c, d, fill="springgreen", outline="black")
def move_square1(event):
    if event.keysym == 'Left':
        canvas.move(cursor, -200, 0)
    elif event.keysym == 'Right':
        canvas.move(cursor, 200, 0)
    elif event.keysym == 'Up':
        canvas.move(cursor, 0, -200)
    elif event.keysym == 'Down':
        canvas.move(cursor, 0, 200)
for x in range(100):
    canvas.bind_all('<KeyPress-Left>', move_square1)
    canvas.bind_all('<KeyPress-Right>', move_square1)
    canvas.bind_all('<KeyPress-Up>', move_square1)
    canvas.bind_all('<KeyPress-Down>', move_square1)
canvas.mainloop()
