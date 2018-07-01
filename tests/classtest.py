#! /usr/bin/python3

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600, bd=0, highlightthickness=0)
class Object:
    def __init__(self, color, size):
        colors = ['blue2', 'red', 'green2', 'yellow']
