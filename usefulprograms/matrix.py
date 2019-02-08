#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700, bg="aqua", bd=0, highlightthickness=0)
canvas.pack()

width1 = int(input("Enter width of matrices: "))
height1 = int(input("Enter height of matrices: "))
operator = input("multiply(x), add(+) or subtract(-): ")

if operator == "+" or operator == "-":
    width2 = width1
    height2 = height1
elif operator == "x":
    height2 = width1
    width2 = height1

var1 = StringVar()
label = Label(tk, textvariable=var1, relief=FLAT, height=height1+4, width=3, bg="orange", font=("arial", 12, "bold"))
var1.set("__" + ("\n|"*height1) + "__")
label.pack()

var2 = StringVar()
label2 = Label(tk, textvariable=var2, relief=FLAT, height=height1+4, width=3, bg="lightgreen", font=("arial", 12, "bold"))
var2.set("__\n" + ("  |\n"*height1) + "__")
label2.pack()

var3 = StringVar()
label3 = Label(tk, textvariable=var3, relief=FLAT, height=height2+4, width=3, bg="purple", font=("arial", 12, "bold"))
var3.set("__" + ("\n|"*height2) + "__")
label3.pack()

var4 = StringVar()
label4 = Label(tk, textvariable=var4, relief=FLAT, height=height2+4, width=3, bg="blue", font=("arial", 12, "bold"))
var4.set("__\n" + ("  |\n"*height2) + "__")
label4.pack()

canvas.create_window(50, 200, window=label)
canvas.create_window(50+width1*14, 200, window=label2)
canvas.create_window(450, 150, window=label3)
canvas.create_window(450+width2*14, 200, window=label4)
canvas.create_text(250, 200, text=operator, font=("arial", 50), fill="black")

matrix1 = []
matrix2 = []
for x in range(height1):
    matrix1.append([])
for x in range(height1):
    for y in range(width1):
        matrix1[x].append(int(input("Enter next number (1st matrix): ")))
for x in range(height2):
    matrix2.append([])
for x in range(height2):
    for y in range(width2):
        matrix2[x].append(int(input("Enter next number (2nd matrix): ")))
canvas.mainloop()
