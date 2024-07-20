#! /usr/bin/python3

WIDTH = 900
HEIGHT = 800

# Object on road - ex. coin, box
class RoadObj:
    def __init__(self, edges, xPosRef, yPosRef):
        # xPosRef - horizontal reference point 0 = start of left lane, 1 = end of right lane
        self.xPosRef = xPosRef
        # yPosRef - vertical reference point 0 = top of road, 1 = bottom of road
        self.yPosRef = yPosRef
        # edges - list of vector tuples of edges (x1, y1, x2, y2) - all 0-1
        self.edges = edges
        # canvasCoords - list of coordinates of edges on canvas
        self.canvasCoords = []
    def getCanvasCoords(self):
        self.canvasCoords = []
        # Convert edges of road items (box or coin) to coordinates on canvas
        for edge in self.edges:
            # Start of left lane at top y-coordinate
            leftLaneStart = WIDTH*(8 - 3*(self.yPosRef + edge[1]))/20  # 2*WIDTH/5 - (3*WIDTH/20)*(self.yPosRef + edge[1])
            # Width of road at top y-coordinate
            roadWidth = WIDTH*(2 + 3*(self.yPosRef + edge[1]))/10 # WIDTH/5 + (3*WIDTH/10)*(self.yPosRef + edge[1])
            # Start of left lane at bottom y-coordinate
            leftLaneStart2 = WIDTH*(8 - 3*(self.yPosRef + edge[3]))/20
            # Width of road at top y-coordinate
            roadWidth2 = WIDTH*(2 + 3*(self.yPosRef + edge[3]))/10
            # Convert edge of box or coin to coordinates on canvas given leftLaneStart, leftLaneStart2, roadWidth and roadWidth2
            xCoord1 = leftLaneStart + roadWidth * self.xPosRef + roadWidth * edge[0]
            xCoord2 = leftLaneStart2 + roadWidth2 * self.xPosRef + roadWidth2 * edge[2]
            yCoord1 = HEIGHT * self.yPosRef + HEIGHT * edge[1]
            yCoord2 = HEIGHT * self.yPosRef + HEIGHT * edge[3]
            # Store coordinates
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

# Coordinates of road items relative to road width and height 0=top/left, 1=bottom/right
boxEdges = [(0, 0, (1/3), 0), ((1/3), 0, (1/3), (1/6)), ((1/3), (1/6), 0, (1/6)), (0, (1/6), 0, 0)]
coinEdges = [((1/6), (1/24), (2/9), (1/18)), ((2/9), (1/18), (1/4), (1/12)), ((1/4), (1/12), (2/9), (1/9)),\
            ((2/9), (1/9), (1/6), (1/8)), ((1/6), (1/8), (1/9), (1/9)), ((1/9), (1/9), (1/12), (1/12)),\
            ((1/12), (1/12), (1/9), (1/18)), ((1/9), (1/18), (1/6), (1/24))]

# All boxes in game
boxes = []
# Canvas items of boxes
boxSprites = []
# All coins in game
coins = []
# Canvas items of coins
coinSprites = []

# Box colors
colors = ["sienna4", "DarkOrange4", "coral4", "tan2", "gold4", "honeydew4", "saddle brown", "SkyBlue4", "gray50", "tomato4"] * 60
random.shuffle(colors)

# Draw boxes and coins at current position (most are off screen)
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

# Initial scoreboard
scoreBoard = canvas.create_text(WIDTH/2, HEIGHT/10, text="Score: 0", font=("helvetica", 20), fill="navy")

# Human stick figure canvas objects
human = []
human.append(canvas.create_line(WIDTH*0.475, HEIGHT*0.95, WIDTH*0.5, HEIGHT*0.90, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.525, HEIGHT*0.95, WIDTH*0.5, HEIGHT*0.90, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.5, HEIGHT*0.90, WIDTH*0.5, HEIGHT*0.80, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.475, HEIGHT*0.85, WIDTH*0.5, HEIGHT*0.80, fill="black", width=4))
human.append(canvas.create_line(WIDTH*0.525, HEIGHT*0.85, WIDTH*0.5, HEIGHT*0.80, fill="black", width=4))
human.append(canvas.create_rectangle(WIDTH*0.49, HEIGHT*0.76, WIDTH*0.51, HEIGHT*0.80, fill="black"))

# 1 = left lane, 2 = middle lane, 3 = right lane
humanLane = 2
# Canvas y-position of human relative to rest position, 0 = ground
humanJumpHeight = 0
# Change in y-position per frame during jump
humanJumpIncrement = -HEIGHT*0.08
# False = user did not press jump key, True = user pressed jump key
jump = False
# Whether user has lost game
lost = False

# Keyboard events for human
def move_human(event):
    global humanLane
    global jump
    if event.keysym == 'Left':
        # Move left 1 lane within bounds
        humanLane -= 1
        if humanLane < 1:
            humanLane = 1
    elif event.keysym == 'Right':
        # Move right 1 lane within bounds
        humanLane += 1
        if humanLane > 3:
            humanLane = 3
    elif event.keysym == 'Up':
        # When jump = True, height above ground increases and decreases during certain amount of frames
        jump = True
canvas.bind_all('<KeyPress-Left>', move_human)
canvas.bind_all('<KeyPress-Right>', move_human)
canvas.bind_all('<KeyPress-Up>', move_human)

# Total number of boxes passed (moved below height of screen)
boxesPassedCnt = 0
# Box objects that have been passed
boxesPassed = []
# Total number of coins passed
coinsPassedCnt = 0
# Coin objects that have been passed
coinsPassed = []
# Coin objects that have been collected
collectedCoins = []
# Score, constantly increases until game over
score = 0
# Coin score, increases when coin is collected
coinScore = 0

# Loop through each frame
# 1 frame - Road objects move 1/30 * height of screen
# Full game - Length of visible frame * 54
for x in range(30*54):
    # Move every single box (including ones not visible in current frame), track boxes passed and coordinates
    # 3 boxes per frame
    for y in range(162):
        boxes[y].yPosRef += (1/30)
        c = boxes[y].getCanvasCoords()
        canvas.coords(boxSprites[y], c[0][0], c[0][1], c[1][0], c[1][1], c[2][0], c[2][1], c[3][0], c[3][1])
        if c[2][1] > 0 and boxes[y] not in boxesPassed:
            boxesPassedCnt += 1
            boxesPassed.append(boxes[y])
    # Move every single coin (including ones not visible in current frame), track coins passed and coordinates
    # 2 coins per frame
    for y in range(108):
        coins[y].yPosRef += (1/30)
        c2 = coins[y].getCanvasCoords()
        canvas.coords(coinSprites[y], c2[0][0], c2[0][1], c2[1][0], c2[1][1], c2[2][0], c2[2][1], c2[3][0], c2[3][1], c2[4][0], c2[4][1], c2[5][0], c2[5][1], c2[6][0], c2[6][1], c2[7][0], c2[7][1])
        if c2[4][1] > 0 and coins[y] not in coinsPassed:
            coinsPassedCnt += 1
            coinsPassed.append(coins[y])
    # Update coordinates of human to account for lane (1, 2 or 3)
    canvas.coords(human[0], WIDTH*0.475+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[0])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[0])[3])
    canvas.coords(human[1], WIDTH*0.525+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[1])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[1])[3])
    canvas.coords(human[2], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[2])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[2])[3])
    canvas.coords(human[3], WIDTH*0.475+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[3])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[3])[3])
    canvas.coords(human[4], WIDTH*0.525+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[4])[1], WIDTH*0.5+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[4])[3])
    canvas.coords(human[5], WIDTH*0.49+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[5])[1], WIDTH*0.51+((humanLane-2)*WIDTH*(8 - 3*0.95)/20)/2, canvas.coords(human[5])[3])
    # Move up and down for certain number of frames when jump key is pressed
    if jump:
        for i in human:
            canvas.move(i, 0, humanJumpIncrement)
        humanJumpHeight -= humanJumpIncrement
        if humanJumpHeight == HEIGHT*0.72:
            humanJumpIncrement = -humanJumpIncrement
        if humanJumpHeight == 0 and humanJumpIncrement > 0:
            humanJumpIncrement = -humanJumpIncrement
            jump = False
    # Track whether human is touching a box or coin, end game or change scoreboard and track progress accordingly
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
    # Maximum score is 100000, reached once player finishes all frames
    score = math.floor(x / (54*30-1) * 100000)
    # Show score and number of coins collected compared to total number of coins passed
    canvas.itemconfig(scoreBoard, text=("Score: " + str(score) + " Coins: " + str(coinScore) + "/" + str(coinsPassedCnt)))
    tk.update()
    time.sleep(0.01)
    if lost:
        break

if lost:
    # Hit a box before completing all frames
    canvas.create_text(WIDTH/2, HEIGHT/2, text=("You lost. Score: " + str(score)), font=("helvetica", 50), fill="navy")
else:
    # Completed all frames without touching any boxes
    canvas.create_text(WIDTH/2, HEIGHT/2, text=("You won. Score: " + str(score)), font=("helvetica", 50), fill="navy")

canvas.mainloop()
