#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=1000)
canvas.pack()
x = 20
y = 20
def write(event):
    x = 20
    y = 20
    while True:
        if event.char == "a":
            canvas.create_text(x, y, text="a")
            x = x + 20
        if event.char == "b":
            canvas.create_text(x, y, text="b")
            x = x + 20
        if event.char == "c":
            canvas.create_text(x, y, text="c")
            x = x + 20
        if event.char == "d":
            canvas.create_text(x, y, text="d")
            x = x + 20
        if event.char == "e":
            canvas.create_text(x, y, text="e")
            x = x + 20
        if event.char == "f":
            canvas.create_text(x, y, text="f")
            x = x + 20
        if event.char == "g":
            canvas.create_text(x, y, text="g")
            x = x + 20
        if event.char == "h":
            canvas.create_text(x, y, text="h")
            x = x + 20
        if event.char == "i":
            canvas.create_text(x, y, text="i")
            x = x + 20
        if event.char == "j":
            canvas.create_text(x, y, text="j")
            x = x + 20
        if event.char == "k":
            canvas.create_text(x, y, text="k")
            x = x + 20
        if event.char == "l":
            canvas.create_text(x, y, text="l")
            x = x + 20
        if event.char == "m":
            canvas.create_text(x, y, text="m")
            x = x + 20
        if event.char == "n":
            canvas.create_text(x, y, text="n")
            x = x + 20
        if event.char == "o":
            canvas.create_text(x, y, text="o")
            x = x + 20
        if event.char == "p":
            canvas.create_text(x, y, text="p")
            x = x + 20
        if event.char == "q":
            canvas.create_text(x, y, text="q")
            x = x + 20
        if event.char == "r":
            canvas.create_text(x, y, text="r")
            x = x + 20
        if event.char == "s":
            canvas.create_text(x, y, text="s")
            x = x + 20
        if event.char == "t":
            canvas.create_text(x, y, text="t")
            x = x + 20
        if event.char == "u":
            canvas.create_text(x, y, text="u")
            x = x + 20
        if event.char == "v":
            canvas.create_text(x, y, text="v")
            x = x + 20
        if event.char == "w":
            canvas.create_text(x, y, text="w")
            x = x + 20
        if event.char == "x":
            canvas.create_text(x, y, text="x")
            x = x + 20
        if event.char == "y":
            canvas.create_text(x, y, text="y")
            x = x + 20
        if event.char == "z":
            canvas.create_text(x, y, text="z")
            x = x + 20
canvas.mainloop()
