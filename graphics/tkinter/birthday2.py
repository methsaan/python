#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600, bg="lightgreen", bd=0, highlightthickness=0)
canvas.pack()
shade = "gray95"
canvas.create_text(300, 300, fill=shade, text="Happy birthday", font=('helvetica', 40))
a = 500
b = 0
c = 600
d = 100
transparency = 95
for x in range(168):
    colors1 = random.choice(['green', 'green2', 'green3', 'green4', 'springgreen', 'forestgreen', 'lightgreen', 'darkgreen', 'greenyellow', 'yellowgreen'])
    colors2 = random.choice(['blue', 'aqua', 'lightblue', 'blue2', 'blue3', 'blue4', 'navy'])
    canvas.create_rectangle(a, b, c, d, fill=colors1, outline=colors2)
    tk.update()
    a = a - 3
    b = b + 3
    c = c - 3
    d = d + 3
    transparency -= 6
    if transparency <= 0:
        transparency = 95
    shade = "gray" + str(transparency)
    canvas.create_text(300, 300, fill=shade, text="Happy birthday", font=('helvetica', 40))
    tk.update()
canvas.mainloop()
