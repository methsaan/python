#! /usr/bin/python3

from tkinter import *

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = []
