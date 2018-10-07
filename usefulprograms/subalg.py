#! /usr/bin/python3

import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg="blue2", bd=0, highlightthickness=0)
canvas.pack()

canvas.create_rectangle(0, 0, 500, 500, fill="blue")
x = int(input("Enter a three digit number: "))
y = int(input("Enter another three digit number: "))

str1=""
str2=""
str3=""
ones1 = x%10
tens1 = int(((x%100)-ones1)/10)
hundreds1 = int((x-(x%100))/100)
ones2 = y%10
tens2 = int(((y%100)-ones2)/10)
hundreds2 = int((y-(y%100))/100)
ones = ones1 - ones2
tens = tens1 - tens2
if ones < 0:
    str1=str(ones1+10)
    str2=str(tens1-1)
    str3=hundreds1
    ones=int(str1)-ones2
else:
    str1=" "
if tens < 0:
    if str2 != "":
        str2 = str(int(str2)+10)
    str3=str(hundreds1-1)
    if str2 != "":
        tens=int(str2)-tens2
    else:
        tens=tens1-tens2
canvas.create_text(228, 170, text=str3, font=("times", 15), fill="orange")
canvas.create_text(250, 170, text=str2, font=("times", 15), fill="orange")
canvas.create_text(272, 170, text=str1, font=("times", 15), fill="orange")
canvas.create_text(250, 200, text=str(hundreds1)+" "+str(tens1)+" "+str(ones1), font=("times", 25), fill="orange")
canvas.create_text(250, 240, text=str(hundreds2)+" "+str(tens2)+" "+str(ones2), font=("times", 25), fill="orange")
canvas.create_line(200, 260, 300, 260, width=4, fill="orange")
canvas.create_line(195, 245, 205, 245, width=3, fill="orange")
canvas.create_text(250, 280, text=str(int(str3)-hundreds2)+" "+str(int(str2)-tens2)+" "+str(int(str1)-ones2), font=("times", 25), fill="orange")
canvas.mainloop()
