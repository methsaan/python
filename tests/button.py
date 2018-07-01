#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
def hello():
    print("Hello")
button = Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)
hello = tk.Button(frame, text="Hello", command=hello)
hello.pack(side=tk.LEFT)
canvas.mainloop()
