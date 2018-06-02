#! /usr/bin/python3

from tkinter import *
import time
import random

tk = Tk()
canvas = Canvas(tk, width=600, height=600, bg="orange")
monster = canvas.create_rectangle(500, 0, 600, 100, fill="red")
