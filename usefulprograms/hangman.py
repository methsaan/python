#! /usr/bin/python3

import random
import time
import turtle

t = turtle.Pen()

t.width(5)
t.speed(4)

def hangman(strikenum):
    if strikenum == 1:
        t.forward(100)
    if strikenum == 2:
        t.backward(50)
        t.left(90)
        t.forward(100)
    if strikenum == 3:
        t.right(90)
        t.forward(50)
    if strikenum == 4:
        t.right(90)
        t.forward(15)
    if strikenum == 5:
        t.right(90)
        t.circle(10, 540)
    if strikenum == 6:
        t.right(90)
        t.forward(25)
    if strikenum == 7:
        t.right(45)
        t.forward(20)
    if strikenum == 8:
        t.backward(20)
        t.left(90)
        t.forward(20)
    if strikenum == 9:
        t.backward(20)
        t.right(45)
        t.backward(25)
        t.right(45)
        t.forward(20)
    if strikenum == 10:
        t.backward(20)
        t.left(90)
        t.forward(20)
    else:
        pass
for x in range(10):
    hangman(x+1)
time.sleep(10)
