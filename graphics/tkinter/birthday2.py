#! /usr/bin/python3

import random
import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600, bg="black")
canvas.pack()
shade = "gray95"
canvas.create_text(300, 300, fill=shade, text="Happy birthday", font=('helvetica', 40))
a = 500
b = 0
c = 600
d = 100
transparency = 95
for x in range(500):
    colors1 = random.choice(['blue', 'red', 'yellow', 'orange', 'purple', 'green2', 'aqua'])
    colors2 = random.choice(['blue', 'red', 'yellow', 'orange', 'purple', 'green2', 'aqua'])
    canvas.create_rectangle(a, b, c, d, fill=colors1, outline=colors2)
    tk.update()
    a = a - 1
    b = b + 1
    c = c - 1
    d = d + 1
    transparency -= 2
    if transparency <= 0:
        transparency = 95
    shade = "gray" + str(transparency)
    canvas.create_text(300, 300, fill=shade, text="Happy birthday", font=('helvetica', 40))
    time.sleep(0.001)
    tk.update()
canvas.mainloop()
