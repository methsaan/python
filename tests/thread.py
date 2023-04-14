#! /usr/bin/python3

import tkinter, threading, time

def real_time(td, canvas):
    while True:
        time.sleep(1/60.0)
        canvas.coords('line',1,1,200,200)

def func(event):
    print("key pressed")


root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()
canvas.create_line(1,1,100,100, tag='line')
root.bind('<Right>', func)
thread = threading.Thread(target = real_time, args = (1/60.0, canvas))
thread.start()
root.mainloop()
