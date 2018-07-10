#! /usr/bin/python3

import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0, bg="white")
canvas.pack()
tk.title("Press i for instructions")
at = [250, 250, "red", 1, 5, canvas.create_oval(240, 240, 260, 260, fill="black", outline="black")]
def movePen(event):
    if event.keysym == "Up":
        canvas.move(at[5], 0, -at[4])
        canvas.create_line(at[0], at[1], at[0], at[1]-at[4], fill=at[2], width=at[3])
        at[1] -= at[4]
    elif event.keysym == "Down":
        canvas.move(at[5], 0, at[4])
        canvas.create_line(at[0], at[1], at[0], at[1]+at[4], fill=at[2], width=at[3])
        at[1] += at[4]
    elif event.keysym == "Left":
        canvas.move(at[5], -at[4], 0)
        canvas.create_line(at[0], at[1], at[0]-at[4], at[1], fill=at[2], width=at[3])
        at[0] -= at[4]
    elif event.keysym == "Right":
        canvas.move(at[5], at[4], 0)
        canvas.create_line(at[0], at[1], at[0]+at[4], at[1], fill=at[2], width=at[3])
        at[0] += at[4]
    elif event.keysym == "Return":
        at[2] = random.choice(["red", "orange", "darkgoldenrod", "springgreen", "aqua", "purple", "black", "blue", "gray", "green"])
    elif event.keysym == "space":
        at[2] = ""
    elif event.char == "e":
        at[2] = "white"
    elif event.char == "w":
        at[3] += 2
    elif event.char == "o":
        at[4] += 5
    elif event.char == "h":
        usercol = input("Enter color: ")
        at[2] = usercol
    elif event.char == "c":
        canvas.create_rectangle(0, 0, 500, 500, fill="white", outline="white")
    elif event.char == "r":
        at[0] = 250
        at[1] = 250
        at[2] = "red"
        at[3] = 1
        at[4] = 5
        canvas.create_rectangle(0, 0, 500, 500, fill="white", outline="white")
        at[5] = canvas.create_rectangle(240, 240, 260, 260)
    elif event.char == "t":
        at[3] -= 2
    elif event.char == "s":
        at[4] -= 5
    elif event.char == "i":
        print("Manual for \"draw.py\":")
        print("Return: pick random color")
        print("t: decrease speed of pen, s: decrease width of pen")
        print("w: increase width of pen, r: reset canvas, e: erase")
        print("o: increase speed of pen, spacebar: change pen color to transparent")
        print("h: change pen color by input")
canvas.bind_all("<KeyPress-Up>", movePen)
canvas.bind_all("<KeyPress-Down>", movePen)
canvas.bind_all("<KeyPress-Left>", movePen)
canvas.bind_all("<KeyPress-Right>", movePen)
canvas.bind_all("<KeyPress-Return>", movePen)
canvas.bind_all("<space>", movePen)
canvas.bind_all("<KeyPress-e>", movePen)
canvas.bind_all("<KeyPress-w>", movePen)
canvas.bind_all("<KeyPress-o>", movePen)
canvas.bind_all("<KeyPress-s>", movePen)
canvas.bind_all("<KeyPress-c>", movePen)
canvas.bind_all("<KeyPress-r>", movePen)
canvas.bind_all("<KeyPress-d>", movePen)
canvas.bind_all("<KeyPress-s>", movePen)
canvas.bind_all("<KeyPress-i>", movePen)
canvas.mainloop()
