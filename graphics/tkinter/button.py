#! /usr/bin/python3

import tkinter as tkx
x = "blue"
def write_slogan():
    x = "red"
b = tkx.Tk()
frame = tkx.Frame(b, width=700, height=700)
frame.pack()
slogan = tkx.Button(frame, text="Hello", command=write_slogan)
slogan.pack(side=tkx.LEFT)
print(x)
b.mainloop()
