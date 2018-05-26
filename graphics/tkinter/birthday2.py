#! /usr/bin/python3

import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600, bg="white")
canvas.pack()
shade = "gray95"
canvas.create_text(300, 300, fill=shade, text="Happy birthday", font=('helvetica', 40))
a = 500
b = 0
c = 600
d = 100
canvas.create_rectangle(a, b, c, d, fill="blue2", outline="blue4")
canvas.mainloop()
