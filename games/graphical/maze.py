#! /usr/bin/python3

import subprocess as sp
import random
import time
from tkinter import *
tk = Tk()
tk.title("Reach the safe box without touching the bombs")
canvas = Canvas(tk, width=800, height=800, bg="white", bd=0, highlightthickness=0)
canvas.pack()

class Man():
    def __init__(self):
        self.head = canvas.create_oval(40, 40, 60, 60, fill="red", outline="")
        self.body = canvas.create_line(50, 50, 50, 125, width=5, fill="red")
        self.arm1 = canvas.create_line(30, 80, 70, 80, width=5, fill="red")
        self.leg1 = canvas.create_line(50, 125, 25, 150, width=5, fill="red")
        self.leg2 = canvas.create_line(50, 125, 75, 150, width=5, fill="red")
        self.fullbody = [self.head, self.body, self.arm1, self.leg1, self.leg2]
        self.positions = [canvas.coords(self.arm1)[0]+5, canvas.coords(self.head)[1]+5, canvas.coords(self.arm1)[2]-5, canvas.coords(self.leg1)[3]-5]
    def move(self, direction, amount):
        if direction == "Left" or direction == "Right":
            for x in self.fullbody:
                canvas.move(x, amount if direction == "Right" else -amount, 0)
        else:
            for x in self.fullbody:
                canvas.move(x, 0, amount if direction == "Down" else -amount)
        self.positions = [canvas.coords(self.arm1)[0], canvas.coords(self.head)[1]-10, canvas.coords(self.arm1)[2], canvas.coords(self.leg1)[3]]
class Box():
    def __init__(self, size, x, y, color):
        self.size = size
        self.box = canvas.create_rectangle(x-size/2, y-size/2, x+size/2, y+size/2, fill=color, outline=color)
        self.positions = [canvas.coords(self.box)[0]-size/2, canvas.coords(self.box)[1]-size/2, canvas.coords(self.box)[2]+size/2, canvas.coords(self.box)[3]+size/2]
    def move(self, direction, amount):
        if direction == "Left" or direction == "Right":
            canvas.move(self.box, amount if direction == "Right" else -amount, 0)
        else:
            canvas.move(self.box, 0, amount if direction == "Down" else -amount)
        self.positions = [canvas.coords(self.box)[0]-self.size/2, canvas.coords(self.box)[1]-self.size/2, canvas.coords(self.box)[2]+self.size/2, canvas.coords(self.box)[3]+self.size/2]
player = Man()
destination = canvas.create_rectangle(695, 695, 795, 795, width=10, outline="blue")
tk.update()
boxes = []
for x in range(30):
    boxSize = random.randrange(46, 92)
    if random.choice([True, False]):
        xCoord = random.randrange(boxSize+75, 695-boxSize)
        yCoord = random.randrange(boxSize+75, 795-boxSize)
    else:
        xCoord = random.randrange(boxSize+75, 795-boxSize)
        yCoord = random.randrange(boxSize+75, 695-boxSize)
    boxes.append(Box(boxSize, xCoord, yCoord, "black"))
tk.update()
cnt = 0
running = True
lost = False
def moveMan(event):
    if event.keysym == 'Left':
        player.move("Left", 40)
    if event.keysym == 'Right':
        player.move("Right", 40)
    if event.keysym == 'Up':
        player.move("Up", 40)
    if event.keysym == 'Down':
        player.move("Down", 40)
    if event.keysym == 'Return':
        running = True
    canvas.bind_all("<KeyPress-Up>", moveMan)
    canvas.bind_all("<KeyPress-Down>", moveMan)
    canvas.bind_all("<KeyPress-Left>", moveMan)
    canvas.bind_all("<KeyPress-Right>", moveMan)
    canvas.bind_all("<KeyPress-Return>", moveMan)
won = False
while running:
    def moveMan(event):
        if event.keysym == 'Left':
            player.move("Left", 40)
        if event.keysym == 'Right':
            player.move("Right", 40)
        if event.keysym == 'Up':
            player.move("Up", 40)
        if event.keysym == 'Down':
            player.move("Down", 40)
        if event.keysym == 'Return':
            running = True
    canvas.bind_all("<KeyPress-Up>", moveMan)
    canvas.bind_all("<KeyPress-Down>", moveMan)
    canvas.bind_all("<KeyPress-Left>", moveMan)
    canvas.bind_all("<KeyPress-Right>", moveMan)
    canvas.bind_all("<KeyPress-Return>", moveMan)
    tk.update()
    if canvas.coords(player.arm1)[0] < 0:
        player.move("Right", abs(canvas.coords(player.arm1)[0]))
    tk.update()
    if canvas.coords(player.arm1)[2] > 800:
        player.move("Left", abs(800-canvas.coords(player.arm1)[2]))
    tk.update()
    if canvas.coords(player.head)[1] < 0:
        player.move("Down", abs(canvas.coords(player.head)[1]))
    tk.update()
    if canvas.coords(player.leg1)[3] > 800:
        player.move("Up", abs(800-canvas.coords(player.leg1)[3]))
    tk.update()
    for box in boxes:
        if canvas.coords(box.box)[0] < 0:
            box.move("Right", abs(canvas.coords(box.box)[0]))
        tk.update()
        if canvas.coords(box.box)[2] > 800:
            box.move("Left", abs(800-canvas.coords(box.box)[2]))
        tk.update()
        if canvas.coords(box.box)[1] < 0:
            box.move("Down", abs(canvas.coords(box.box)[1]))
        tk.update()
        if canvas.coords(box.box)[3] > 800:
            box.move("Up", abs(800-canvas.coords(box.box)[3]))
        tk.update()
    tk.update()
    isInContact = False
    if won and not isInContact:
        running = False
    if not lost and not won:
        for box in boxes:
            if box.positions[2] >= player.positions[0] and box.positions[0] <= player.positions[2] and box.positions[3] >= player.positions[1] and box.positions[1] <= player.positions[3]:
                isInContact = True
                for x in player.fullbody:
                    canvas.itemconfig(x, fill="black")
                    tk.update()
                    time.sleep(0.01)
                for x in player.fullbody:
                    tk.update()
                    time.sleep(0.05)
                    canvas.itemconfig(x, fill="white")
                tk.title("YOU LOST")
                lost = True
            tk.update()
    if isInContact and not won:
        for x in range(20):
            boxSize = random.randrange(46, 92)
            if random.choice([True, False]):
                xCoord = random.randrange(boxSize+75, 695-boxSize)
                yCoord = random.randrange(boxSize+75, 795-boxSize)
            else:
                xCoord = random.randrange(boxSize+75, 795-boxSize)
                yCoord = random.randrange(boxSize+75, 695-boxSize)
            boxes.append(Box(boxSize, xCoord, yCoord, "black"))
        for box in boxes:
            canvas.itemconfig(box.box, fill=random.choice(["red", "orange", "yellow", "orangered"]))
            tk.update()
            time.sleep(0.01)
            canvas.itemconfig(box.box, outline=random.choice(["red", "orange"]))
            tk.update()
            time.sleep(0.01)
    if not lost and canvas.coords(player.arm1)[0] >= 695 and canvas.coords(player.arm1)[0] <= 795 and canvas.coords(player.arm1)[1]-30 >= 695 and canvas.coords(player.arm1)[3]-3 <= 795:
        for x in range(20):
            boxSize = random.randrange(46, 92)
            if random.choice([True, False]):
                xCoord = random.randrange(boxSize+75, 695-boxSize)
                yCoord = random.randrange(boxSize+75, 795-boxSize)
            else:
                xCoord = random.randrange(boxSize+75, 795-boxSize)
                yCoord = random.randrange(boxSize+75, 695-boxSize)
            boxes.append(Box(boxSize, xCoord, yCoord, "black"))
        for x in player.fullbody:
            canvas.itemconfig(x, fill="gold")
        won = True
        tk.title("YOU WON")
    cnt = 0
    if cnt%5 == 0:
        for box in boxes:
            direction = random.choice(["Left", "Right", "Up", "Down"])
            for x in range(30):
                box.move(direction, 2)
                tk.update()
        tk.update()
    cnt = cnt + 1
canvas.mainloop()
