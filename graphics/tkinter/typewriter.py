#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvases = [Canvas(tk, width=500, height=1000), 20, 20]
canvases[0].pack()

def write(event):
    if event.keysym == "Return":
        canvases[1] = 20
        canvases[2] = canvases[2] + 10
    if event.char == "a":
        canvases[0].create_text(canvases[1], canvases[2], text="a", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "b":
        canvases[0].create_text(canvases[1], canvases[2], text="b", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "c":
        canvases[0].create_text(canvases[1], canvases[2], text="c", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "d":
        canvases[0].create_text(canvases[1], canvases[2], text="d", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "e":
        canvases[0].create_text(canvases[1], canvases[2], text="e", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "f":
        canvases[0].create_text(canvases[1], canvases[2], text="f", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "g":
        canvases[0].create_text(canvases[1], canvases[2], text="g", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "h":
        canvases[0].create_text(canvases[1], canvases[2], text="h", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "i":
        canvases[0].create_text(canvases[1], canvases[2], text="i", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "j":
        canvases[0].create_text(canvases[1], canvases[2], text="j", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "k":
        canvases[0].create_text(canvases[1], canvases[2], text="k", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "l":
        canvases[0].create_text(canvases[1], canvases[2], text="l", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "m":
        canvases[0].create_text(canvases[1], canvases[2], text="m", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "n":
        canvases[0].create_text(canvases[1], canvases[2], text="n", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "o":
        canvases[0].create_text(canvases[1], canvases[2], text="o", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "p":
        canvases[0].create_text(canvases[1], canvases[2], text="p", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "q":
        canvases[0].create_text(canvases[1], canvases[2], text="q", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "r":
        canvases[0].create_text(canvases[1], canvases[2], text="r", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "s":
        canvases[0].create_text(canvases[1], canvases[2], text="s", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "t":
        canvases[0].create_text(canvases[1], canvases[2], text="t", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "u":
        canvases[0].create_text(canvases[1], canvases[2], text="u", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "v":
        canvases[0].create_text(canvases[1], canvases[2], text="v", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "w":
        canvases[0].create_text(canvases[1], canvases[2], text="w", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "x":
        canvases[0].create_text(canvases[1], canvases[2], text="x", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "y":
        canvases[0].create_text(canvases[1], canvases[2], text="y", fill="red", font=("helvetica", 10))
        canvases[1] = canvases[1] + 10
        if canvases[1] > 480:
            canvases[2] = canvases[2] + 10
            canvases[1] = 20
    if event.char == "z":
        canvases[0].create_text(canvases[1], canvases[2], text="z", fill="red", font=("helvetica", 10))
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
