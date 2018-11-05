#! /usr/bin/python3

import time
import random
from tkinter import *
tk = Tk()

c = []
for i in range(1, 10):
    a = Canvas(tk, width=random.randrange(50, 400), height=random.randrange(50, 400), bg="black")
    c.append(a)
    a.pack()
for j in c:
    f = j.create_rectangle(0, 0, 20, 20, fill="white")
    for q in range(8):
        time.sleep(0.02)
        j.move(f, 12, 12)
        tk.update()
for k in c:
    k.mainloop()
