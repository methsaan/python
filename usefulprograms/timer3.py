#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()

import time

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

seconds = int(input("How long (seconds)? "))
startTime = time.time()*1000
secondsPassed = 0
cnt = 0

while True:
    currentTimeTemp = time.time()*1000
    secondsPassed = round((currentTimeTemp-startTime)/1000)
    canvas.create_text(300, 300, text=str(seconds-secondsPassed), font=("helvetica", 60))
    tk.update()
    cnt += 1
    canvas.create_rectangle(0, 0, 600, 600, fill=_from_rgb((0, 50, 100)))


canvas.mainloop()
