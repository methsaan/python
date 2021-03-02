#! /usr/bin/python3

import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg="brown", bd=0, highlightthickness=0)
canvas.pack()

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
hundreds = hundreds1 - hundreds2
if hundreds < 0:
    str3 = "-"
else:
    if ones < 0:
        str1 = str(ones1+10)
        str2 = str(tens1-1)
        str3 = ""
    if tens < 0:
        if ones < 0:
            str2 = str(int(str2)+10)
            str3 = str(hundreds1-1)
        else:
            str1 = str(ones1)
            str2 = str(tens1+10)
            str3 = str(hundreds1-1)
    if hundreds < 0:
        if tens < 0:
            str1 = str(ones1)
            str2 = str(tens1+10)
            str3 = str(hundreds1-1)
        else:
            str1 = str(ones1)
            str2 = str(tens1)
            str3 = str(hundreds1)
if str3 == "":
    str3 = str(hundreds1)
if str2 == "":
    str2 = str(tens1)
if str1 == "":
    str1 = str(ones1)
if str3 == "-":
    str3 = str(hundreds1)
    str2 = str(tens1)
    str1 = str(ones1)
    print("haho!")
if int(str3) != hundreds1:
    canvas.create_text(224, 170, text=str3, font=("helvetica", 15), fill="tomato")
else:
    canvas.create_text(224, 170, text=" ", font=("helvetica", 15), fill="tomato")
if int(str2) != tens1:
    canvas.create_text(250, 170, text=str2, font=("helvetica", 15), fill="tomato")
else:
    canvas.create_text(250, 170, text=" ", font=("helvetica", 15), fill="tomato")
if int(str1) != ones1:
    canvas.create_text(276, 170, text=str1, font=("helvetica", 15), fill="tomato")
else:
    canvas.create_text(276, 170, text=" ", font=("helvetica", 15), fill="tomato")
canvas.create_text(250, 200, text=str(hundreds1)+" "+str(tens1)+" "+str(ones1), font=("helvetica", 25), fill="tomato")
canvas.create_text(250, 240, text=str(hundreds2)+" "+str(tens2)+" "+str(ones2), font=("helvetica", 25), fill="tomato")
canvas.create_line(200, 260, 300, 260, width=4, fill="tomato")
canvas.create_line(195, 245, 205, 245, width=3, fill="tomato")
# negative hundreds
if int(str1) == ones1 and int(str2) == tens1 and int(str3) == hundreds1:
    canvas.create_text(250, 280, text=str(-abs(hundreds1-hundreds2))+" "+str(abs(tens1-tens2))+" "+str(abs(ones1-ones2)), font=("helvetica", 25), fill="tomato")
else:
    canvas.create_text(250, 200, text=str(int(str3)-hundreds2+" "+str(int(str2)-tens2)+" "+str(int(str1)-ones2), font=("helvetica", 25), fill="tomato")
canvas.mainloop()
