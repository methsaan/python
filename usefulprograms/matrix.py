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
label = Label(tk, textvariable=var1, relief=FLAT, height=20, width=32, bg="aqua", font=("arial", 12, "bold"))
var1.set("___" + (" "*((width1+4)*3)) + "___\n" + (("|" + (" " * ((width1+7)*3)) + "|\n")*((height1-1)*2+1)) + "|__" + (" " * ((width1+4)*3)) + "__|")
label.pack()
var2 = StringVar()
label2 = Label(tk, textvariable=var2, relief=FLAT, height=20, width=32, bg="aqua", font=("arial", 12, "bold"))
var2.set("___" + (" "*((width2+4)*3)) + "___\n" + (("|" + (" " * ((width2+7)*3)) + "|\n")*((height2-1)*2+1)) + "|__" + (" " * ((width2+4)*3)) + "__|")

label2.pack()

canvas.create_window(150, 200, window=label)
canvas.create_window(550, 200, window=label2)
canvas.create_text(350, 200, text=operator, font=("arial", 40), fill="black")

matrix1 = []
matrix2 = []
for x in range(height1):
    matrix1.append([])
for x in range(height1):
    for y in range(width1):
        matrix1[x].append(int(input("Enter next number: ")))
for x in range(len(matrix1)):
    canvas.create_text(150, 200-(height1*2+x*2), text=str(matrix1[x]), font=("helovetica", 40))
canvas.mainloop()
