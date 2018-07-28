#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvases = [Canvas(tk, width=500, height=1000), 20, 20]
canvases[0].pack()
def write(event):
    if event.keysym == "Return":
        canvases[1] = 20
        canvases[2] = canvases[2] + 20
    if event.char == "a":
        canvases[0].create_text(canvases[1], canvases[2], text="a")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "b":
        canvases[0].create_text(canvases[1], canvases[2], text="b")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "c":
        canvases[0].create_text(canvases[1], canvases[2], text="c")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "d":
        canvases[0].create_text(canvases[1], canvases[2], text="d")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "e":
        canvases[0].create_text(canvases[1], canvases[2], text="e")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "f":
        canvases[0].create_text(canvases[1], canvases[2], text="f")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "g":
        canvases[0].create_text(canvases[1], canvases[2], text="g")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "h":
        canvases[0].create_text(canvases[1], canvases[2], text="h")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "i":
        canvases[0].create_text(canvases[1], canvases[2], text="i")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "j":
        canvases[0].create_text(canvases[1], canvases[2], text="j")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "k":
        canvases[0].create_text(canvases[1], canvases[2], text="k")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "l":
        canvases[0].create_text(canvases[1], canvases[2], text="l")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "m":
        canvases[0].create_text(canvases[1], canvases[2], text="m")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "n":
        canvases[0].create_text(canvases[1], canvases[2], text="n")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "o":
        canvases[0].create_text(canvases[1], canvases[2], text="o")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "p":
        canvases[0].create_text(canvases[1], canvases[2], text="p")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "q":
        canvases[0].create_text(canvases[1], canvases[2], text="q")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "r":
        canvases[0].create_text(canvases[1], canvases[2], text="r")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "s":
        canvases[0].create_text(canvases[1], canvases[2], text="s")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "t":
        canvases[0].create_text(canvases[1], canvases[2], text="t")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "u":
        canvases[0].create_text(canvases[1], canvases[2], text="u")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "v":
        canvases[0].create_text(canvases[1], canvases[2], text="v")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "w":
        canvases[0].create_text(canvases[1], canvases[2], text="w")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "x":
        canvases[0].create_text(canvases[1], canvases[2], text="x")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "y":
        canvases[0].create_text(canvases[1], canvases[2], text="y")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "z":
        canvases[0].create_text(canvases[1], canvases[2], text="z")
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.keysym == "space":
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
canvases[0].bind_all("<KeyPress-q>", write)
canvases[0].bind_all("<KeyPress-w>", write)
canvases[0].bind_all("<KeyPress-e>", write)
canvases[0].bind_all("<KeyPress-r>", write)
canvases[0].bind_all("<KeyPress-t>", write)
canvases[0].bind_all("<KeyPress-y>", write)
canvases[0].bind_all("<KeyPress-u>", write)
canvases[0].bind_all("<KeyPress-i>", write)
canvases[0].bind_all("<KeyPress-o>", write)
canvases[0].bind_all("<KeyPress-p>", write)
canvases[0].bind_all("<KeyPress-a>", write)
canvases[0].bind_all("<KeyPress-s>", write)
canvases[0].bind_all("<KeyPress-d>", write)
canvases[0].bind_all("<KeyPress-f>", write)
canvases[0].bind_all("<KeyPress-g>", write)
canvases[0].bind_all("<KeyPress-h>", write)
canvases[0].bind_all("<KeyPress-j>", write)
canvases[0].bind_all("<KeyPress-k>", write)
canvases[0].bind_all("<KeyPress-l>", write)
canvases[0].bind_all("<KeyPress-z>", write)
canvases[0].bind_all("<KeyPress-x>", write)
canvases[0].bind_all("<KeyPress-c>", write)
canvases[0].bind_all("<KeyPress-v>", write)
canvases[0].bind_all("<KeyPress-b>", write)
canvases[0].bind_all("<KeyPress-n>", write)
canvases[0].bind_all("<KeyPress-m>", write)
canvases[0].bind_all("<space>", write)
canvases[0].bind_all("<KeyPress-Return>", write)
canvases[0].mainloop()
