#! /usr/bin/python3

WIDTH = 900
HEIGHT = 800

class RoadObj:
    def __init__(self, edges, xPosRef, yPosRef):
        # xPos - horizontal reference point 0 = start of left lane, 1 = end of right lane
        self.xPosRef = xPosRef
        # yPos - vertical reference point 0 = top of road, 1 = bottom of road
        self.yPosRef = yPosRef
        # edges - list of vector tuples of edges (x1, y1, x2, y2) - all 0-1
        self.edges = edges
        self.canvasCoords = []
    def getCanvasCoords(self):
        self.canvasCoords = []
        for edge in self.edges:
            leftLaneStart = WIDTH*(8 - 3*(self.yPosRef + edge[1]))/20  # 2*WIDTH/5 - (3*WIDTH/20)*(self.yPosRef + edge[1])
            roadWidth = WIDTH*(2 + 3*(self.yPosRef + edge[1]))/10 # WIDTH/5 + (3*WIDTH/10)*(self.yPosRef + edge[1])
            leftLaneStart2 = WIDTH*(8 - 3*(self.yPosRef + edge[3]))/20
            roadWidth2 = WIDTH*(2 + 3*(self.yPosRef + edge[3]))/10
            xCoord1 = leftLaneStart + roadWidth * self.xPosRef + roadWidth * edge[0]
            xCoord2 = leftLaneStart2 + roadWidth2 * self.xPosRef + roadWidth2 * edge[2]
            yCoord1 = HEIGHT * self.yPosRef + HEIGHT * edge[1]
            yCoord2 = HEIGHT * self.yPosRef + HEIGHT * edge[3]
            self.canvasCoords.append((xCoord1, yCoord1, xCoord2, yCoord2))
        return self.canvasCoords
    def getRef(self):
        return (self.xPosRef, self.yPosRef)

import time
import random
import math
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="OliveDrab4")
canvas.pack()

# road
canvas.create_polygon(2*WIDTH/5, 0, 3*WIDTH/5, 0, 3*WIDTH/4, HEIGHT, WIDTH/4, HEIGHT, fill="gray20", outline="gray20")

boxEdges = [(0, 0, (1/3), 0), ((1/3), 0, (1/3), (1/6)), ((1/3), (1/6), 0, (1/6)), (0, (1/6), 0, 0)]
coinEdges = [((1/6), (1/24), (2/9), (1/18)), ((2/9), (1/18), (1/4), (1/12)), ((1/4), (1/12), (2/9), (1/9)),\
            ((2/9), (1/9), (1/6), (1/8)), ((1/6), (1/8), (1/9), (1/9)), ((1/9), (1/9), (1/12), (1/12)),\
            ((1/12), (1/12), (1/9), (1/18)), ((1/9), (1/18), (1/6), (1/24))]

boxes = []
boxSprites = []
coins = []
coinSprites = []

colors = ["sienna4", "DarkOrange4", "coral4", "tan2", "gold4", "honeydew4", "saddle brown", "SkyBlue4", "gray50", "tomato4"] * 60
random.shuffle(colors)

for x in range(54):
    laneStarts = [0, (1/3), (2/3)]
    noCoinLane = random.randrange(3)
    for y in range(3):
        box = RoadObj(boxEdges, laneStarts[y], -54+x+random.randrange(90)/100)
        boxes.append(box)
        c = box.getCanvasCoords()
        boxSprites.append(canvas.create_polygon(c[0][0], c[0][1], c[1][0], c[1][1], c[2][0], c[2][1], c[3][0], c[3][1], fill=colors[x*3+y]))
        if y != noCoinLane:
            coinRefy = random.uniform(box.getRef()[1] + (1/6), x-53.1)
            coin = RoadObj(coinEdges, laneStarts[y], coinRefy)
            coins.append(coin)
            c2 = coin.getCanvasCoords()
            coinSprites.append(canvas.create_polygon(c2[0][0], c2[0][1], c2[1][0], c2[1][1], c2[2][0], c2[2][1], c2[3][0], c2[3][1], c2[4][0], c2[4][1], c2[5][0], c2[5][1], c2[6][0], c2[6][1], c2[7][0], c2[7][1], fill="gold3"))

scoreBoard = canvas.create_text(WIDTH/2, HEIGHT/10, text="Score: 0", font=("helvetica", 20), fill="navy")
human = []
human.append(canvas.create_line(WIDTH*0.475, HEIGHT*0.95, WIDTH*0.5, HEIGHT*0.90, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.525, HEIGHT*0.95, WIDTH*0.5, HEIGHT*0.90, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.5, HEIGHT*0.90, WIDTH*0.5, HEIGHT*0.80, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.475, HEIGHT*0.85, WIDTH*0.5, HEIGHT*0.80, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.525, HEIGHT*0.85, WIDTH*0.5, HEIGHT*0.80, fill="black", width=4))
human.append(canvas.create_rectangle(WIDTH*0.49, HEIGHT*0.76, WIDTH*0.51, HEIGHT*0.80, fill="black"))
humanLane = 2
humanJumpHeight = 0
humanJumpIncrement = -HEIGHT*0.08
jump = False
lost = False

def move_paddle(event):
    global humanLane
    global jump
    if event.keysym == 'Left':
        humanLane -= 1
        if humanLane < 1:
            humanLane = 1
    elif event.keysym == 'Right':
        humanLane += 1
        if humanLane > 3:
            humanLane = 3
    elif event.keysym == 'Up':
        jump = True
canvas.bind_all('<KeyPress-Left>', move_paddle)
canvas.bind_all('<KeyPress-Right>', move_paddle)
canvas.bind_all('<KeyPress-Up>', move_paddle)

boxesPassedCnt = 0
boxesPassed = []
coinsPassedCnt = 0
coinsPassed = []
collectedCoins = []
score = 0
coinScore = 0
for x in range(30*54):
    for y in range(162):
        boxes[y].yPosRef += (1/30)
        c = boxes[y].getCanvasCoords()
        canvas.coords(boxSprites[y], c[0][0], c[0][1], c[1][0], c[1][1], c[2][0], c[2][1], c[3][0], c[3][1])
        if c[2][1] > 0 and boxes[y] not in boxesPassed:
            boxesPassedCnt += 1
            boxesPassed.append(boxes[y])
    for y in range(108):
        coins[y].yPosRef += (1/30)
        c2 = coins[y].getCanvasCoords()
        canvas.coords(coinSprites[y], c2[0][0], c2[0][1], c2[1][0], c2[1][1], c2[2][0], c2[2][1], c2[3][0], c2[3][1], c2[4][0], c2[4][1], c2[5][0], c2[5][1], c2[6][0], c2[6][1], c2[7][0], c2[7][1])
        if c2[4][1] > 0 and coins[y] not in coinsPassed:
            coinsPassedCnt += 1
            coinsPassed.append(coins[y])
    canvas.coords(human[0], WIDTH*0.475+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[0])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[0])[3])
    canvas.coords(human[1], WIDTH*0.525+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[1])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[1])[3])
    canvas.coords(human[2], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[2])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[2])[3])
    canvas.coords(human[3], WIDTH*0.475+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[3])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[3])[3])
    canvas.coords(human[4], WIDTH*0.525+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[4])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[4])[3])
    canvas.coords(human[5], WIDTH*0.49+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[5])[1], WIDTH*0.51+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[5])[3])
    if jump:
        for i in human:
            canvas.move(i, 0, humanJumpIncrement)
        humanJumpHeight -= humanJumpIncrement
        if humanJumpHeight == HEIGHT*0.72:
            humanJumpIncrement = -humanJumpIncrement
        if humanJumpHeight == 0 and humanJumpIncrement > 0:
            humanJumpIncrement = -humanJumpIncrement
            jump = False
    else:
        visibleBoxes = boxesPassed[boxesPassedCnt-6:]
        for i in range(len(visibleBoxes)):
            c = visibleBoxes[i].getCanvasCoords()
            humanPos = canvas.coords(human[0])[2]
            if c[0][0] < humanPos and humanPos < c[1][0] and c[0][1] < HEIGHT*0.95 and HEIGHT*0.95 < c[2][1]:
                lost = True
        visibleCoins = coinsPassed[coinsPassedCnt-6:]
        for i in range(len(visibleCoins)):
            c = visibleCoins[i].getCanvasCoords()
            humanPos = canvas.coords(human[0])[2]
            if c[6][0] < humanPos and humanPos < c[2][0] and c[0][1] < HEIGHT*0.95 and HEIGHT*0.95 < c[4][1] and visibleCoins[i] not in collectedCoins:
                collectedCoins.append(visibleCoins[i])
                canvas.itemconfigure(coinSprites[coins.index(visibleCoins[i])], state="hidden")
                coinScore += 1
    score = math.floor(x / (54*30-1) * 100000)
    canvas.itemconfig(scoreBoard, text=("Score: " + str(score) + " Coins: " + str(coinScore) + "/" + str(coinsPassedCnt)))
    tk.update()
    time.sleep(0.01)
    if lost:
        break

if lost:
    canvas.create_text(WIDTH/2, HEIGHT/2, text=("You lost. Score: " + str(score)), font=("helvetica", 50), fill="navy")
else:
    canvas.create_text(WIDTH/2, HEIGHT/2, text=("You won. Score: " + str(score)), font=("helvetica", 50), fill="navy")

canvas.mainloop()
