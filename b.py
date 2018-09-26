#! /usr/bin/python3
from tkinter import *
ttt = Tk()
methsaan = Canvas(ttt, width=200, height=100)
methsaan.pack()
methsaan.create_rectangle(50, 20, 150, 80, fill="#476042")
methsaan.create_rectangle(65, 35, 135, 65, fill="yellow")
methsaan.create_line(0, 0, 50, 20, fill="#476042", width=3)
methsaan.create_line(0, 100, 50, 80, fill="#476042", width=3)
methsaan.create_line(150,20, 200, 0, fill="#476042", width=3)
methsaan.create_line(150, 80, 200, 100, fill="#476042", width=3)
mainloop()
