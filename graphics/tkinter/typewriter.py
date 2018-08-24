#! /usr/bin/python3

import tkinter as tkx
x = "blue"
def write_slogan():
    x = "red"
b = tkx.Tk()
frame = tkx.Frame(b, width=100, height=100)
frame.pack()
slogan = tkx.Button(frame, text="Hello", command=write_slogan)
slogan.pack(side=tkx.LEFT)
while True:
    print(x)
    b.mainloop()
