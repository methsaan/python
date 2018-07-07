#! /usr/bin/python3

from tkinter import *
import time
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0, bg="black")
canvas.pack()
def main():
    x = 0
    y = 0
    colors = ["red", "aqua", "springgreen", "orangered", "yellowgreen", "greenyellow", "gray", "cyan", "blue2"]
    for i in range(400):
        canvas.create_rectangle(x, y, x+100, y+100, fill=random.choice(colors), outline=random.choice(colors))
        canvas.create_text(250, 250, text="Happy birthday", font=("helvetica", 40), fill="white")
        x += random.randrange(1, 25)
        y += random.randrange(1, 25)
        tk.update()
        time.sleep(0.03)
def doMain(event):
    if (event.keysym == "Return"):
        main()
canvas.bind_all("<KeyPress-Return>", doMain)
canvas.mainloop()
