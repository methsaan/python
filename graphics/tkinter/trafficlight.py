#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
canvas.create_rectangle(0, 0, 600, 600, fill="black")
def topnorm():
    canvas.create_oval(200, 0, 400, 200, fill="red4")
def midnorm():
    canvas.create_oval(200, 200, 400, 400, fill="gold4")
def botnorm():
    canvas.create_oval(200, 400, 400, 600, fill="darkgreen")
def toplit():
    canvas.create_oval(200, 0, 400, 200, fill="red")
def midlit():
    canvas.create_oval(200, 200, 400, 400, fill="yellow")
def botlit():
    canvas.create_oval(200, 400, 400, 600, fill="lawngreen")
x = True
while x == True:
    def quit(event):
        if event.keysym == "Return":
            x = False
    canvas.bind_all('<KeyPress-Return>', quit)
    topnorm()
    midnorm()
    botnorm()
    tk.update()
    toplit()
    tk.update()
    time.sleep(2.5)
    midlit()
    topnorm()
    botnorm()
    tk.update()
    time.sleep(0.45)
    botlit()
    topnorm()
    midnorm()
    tk.update()
    time.sleep(2)
canvas.mainloop()
