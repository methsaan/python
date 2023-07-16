#! /usr/bin/python3

import random
import time

from tkinter import *
from tkinter import ttk

scale = 0.9

tk = Tk()
canvas = Canvas(tk, width=2000*scale, height=1000*scale)
canvas.pack()

canvas.create_line(0, 100*scale, 1600*scale, 100*scale, width=2)
canvas.create_line(0, 900*scale, 1600*scale, 900*scale, width=2)
canvas.create_line(100*scale, 0, 100*scale, 1000*scale, width=2)
canvas.create_line(1500*scale, 0, 1500*scale, 1000*scale, width=2)
canvas.create_line(1600*scale, 0, 1600*scale, 1000*scale, width=2)

for x in range(13):
    canvas.create_line(100*(x+2)*scale, 0, 100*(x+2)*scale, 100*scale, width=2)

for x in range(13):
    canvas.create_line(100*(x+2)*scale, 900*scale, 100*(x+2)*scale, 1000*scale, width=2)

for x in range(7):
    canvas.create_line(0, 100*(x+2)*scale, 100*scale, 100*(x+2)*scale, width=2)

for x in range(7):
    canvas.create_line(1500*scale, 100*(x+2)*scale, 1600*scale, 100*(x+2)*scale, width=2)

class stock:
    def __init__(self, dividend, name, ticker, price, priceLow, priceHigh, activeSeason, industries):
        self.dividend = dividend
        self.name = name
        self.ticker = ticker
        self.price = price
        self.priceLow = priceLow
        self.priceHigh = priceHigh
        self.activeSeason = activeSeason
        self.industries = industries

class player:
    def __init__(self, characterName, playerSymbolName, totIncome, stocksOwned, gamePos, symbolColor):
        self.characterName = characterName
        self.totIncome = totIncome
        self.stocksOwned = stocksOwned
        self.gamePos = gamePos
        self.playerSymbol = []
        if playerSymbolName == "car":
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-30*scale, gamePos[1], gamePos[0]+30*scale, gamePos[1]+20*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-15*scale, gamePos[1]-15*scale, gamePos[0]+15*scale, gamePos[1]+15*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-18*scale, gamePos[1]+20*scale, gamePos[0]-12*scale, gamePos[1]+26*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]+12*scale, gamePos[1]+20*scale, gamePos[0]+18*scale, gamePos[1]+26*scale, fill=symbolColor, outline=symbolColor))
        elif playerSymbolName == "suitcase":
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-30*scale, gamePos[1]-20*scale, gamePos[0]+30*scale, gamePos[1]+20*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-40*scale, gamePos[1]-10*scale, gamePos[0]+40*scale, gamePos[1]+10*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-40*scale, gamePos[1]-20*scale, gamePos[0]-20*scale, gamePos[1]*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-40*scale, gamePos[1], gamePos[0]-20*scale, gamePos[1]+20*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]+20*scale, gamePos[1], gamePos[0]+40*scale, gamePos[1]+20*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]+20*scale, gamePos[1]-20*scale, gamePos[0]+40*scale, gamePos[1], fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-25*scale, gamePos[1]-30*scale, gamePos[0]-20*scale, gamePos[1]-20*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]+20*scale, gamePos[1]-30*scale, gamePos[0]+25*scale, gamePos[1]-20*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-25*scale, gamePos[1]-35*scale, gamePos[0]+25*scale, gamePos[1]-30*scale, fill=symbolColor, outline=symbolColor))
        elif playerSymbolName == "shoe":
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0], gamePos[1]-20*scale, gamePos[0]+30*scale, gamePos[1]+10*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-30*scale, gamePos[1], gamePos[0], gamePos[1]+10*scale, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-30*scale, gamePos[1]-10*scale, gamePos[0]+30*scale, gamePos[1]+10*scale, fill=symbolColor, outline=symbolColor))

class dice:
    def __init__(self):
        self.num = 0
        self.cube = [canvas.create_rectangle(1650*scale, 100*scale, 1750*scale, 200*scale, fill="white", outline="black", width=3), canvas.create_polygon(1650*scale, 100*scale, 1750*scale, 100*scale, 1800*scale, 50*scale, 1700*scale, 50*scale, fill="white", outline="black", width=3), canvas.create_polygon(1750*scale, 100*scale, 1800*scale, 50*scale, 1800*scale, 150*scale, 1750*scale, 200*scale, fill="white", outline="black", width=3)]
        self.dots = []
        for x in range(6):
            x = random.randrange(90)
            self.dots.append(canvas.create_oval(1650*scale, 100*scale+x, 1660*scale, 110*scale+x, fill="black", outline="black"))
        tk.update()
        self.roll()
    def roll(self):
        self.num = random.randrange(1, 7)
        if self.num == 1:
            self.__one()
        elif self.num == 2:
            self.__two()
        elif self.num == 3:
            self.__three()
        elif self.num == 4:
            self.__four()
        elif self.num == 5:
            self.__five()
        else:
            self.__six()
    def __one(self):
        canvas.coords(self.dots[0], 1695*scale, 145*scale, 1705*scale, 155*scale)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="hidden")
        canvas.itemconfigure(self.dots[2], state="hidden")
        canvas.itemconfigure(self.dots[3], state="hidden")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __two(self):
        canvas.coords(self.dots[0], 1660*scale, 110*scale, 1670*scale, 120*scale)
        canvas.coords(self.dots[1], 1730*scale, 180*scale, 1740*scale, 190*scale)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="hidden")
        canvas.itemconfigure(self.dots[3], state="hidden")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __three(self):
        canvas.coords(self.dots[0], 1660*scale, 110*scale, 1670*scale, 120*scale)
        canvas.coords(self.dots[1], 1695*scale, 145*scale, 1705*scale, 155*scale)
        canvas.coords(self.dots[2], 1730*scale, 180*scale, 1740*scale, 190*scale)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="hidden")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __four(self):
        canvas.coords(self.dots[0], 1670*scale, 120*scale, 1680*scale, 130*scale)
        canvas.coords(self.dots[1], 1670*scale, 170*scale, 1680*scale, 180*scale)
        canvas.coords(self.dots[2], 1720*scale, 120*scale, 1730*scale, 130*scale)
        canvas.coords(self.dots[3], 1720*scale, 170*scale, 1730*scale, 180*scale)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="normal")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __five(self):
        canvas.coords(self.dots[0], 1670*scale, 120*scale, 1680*scale, 130*scale)
        canvas.coords(self.dots[1], 1670*scale, 170*scale, 1680*scale, 180*scale)
        canvas.coords(self.dots[2], 1720*scale, 120*scale, 1730*scale, 130*scale)
        canvas.coords(self.dots[3], 1720*scale, 170*scale, 1730*scale, 180*scale)
        canvas.coords(self.dots[4], 1695*scale, 145*scale, 1705*scale, 155*scale)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="normal")
        canvas.itemconfigure(self.dots[4], state="normal")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __six(self):
        canvas.coords(self.dots[0], 1670*scale, 120*scale, 1680*scale, 130*scale)
        canvas.coords(self.dots[1], 1670*scale, 170*scale, 1680*scale, 180*scale)
        canvas.coords(self.dots[2], 1720*scale, 120*scale, 1730*scale, 130*scale)
        canvas.coords(self.dots[3], 1720*scale, 170*scale, 1730*scale, 180*scale)
        canvas.coords(self.dots[4], 1695*scale, 120*scale, 1705*scale, 130*scale)
        canvas.coords(self.dots[5], 1695*scale, 170*scale, 1705*scale, 180*scale)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="normal")
        canvas.itemconfigure(self.dots[4], state="normal")
        canvas.itemconfigure(self.dots[5], state="normal")
        tk.update()

formTk = Tk()
formTk.geometry(str(int(scale*500)) + "x" + str(int(scale*800)))

pStr = [[], [], [], []]
players = []
locations = []

for x in range(15):
    locations.append((1550*scale-(x*100*scale), 950*scale))

for x in range(10):
    locations.append((50*scale, 950*scale-(x*100*scale)))

for x in range(15):
    locations.append((50*scale+(x*100*scale), 50*scale))

for x in range(10):
    locations.append((1550*scale, 50*scale+(x*100*scale)))

def submitPlayers():
    global entry, entry2, entry3, entry4
    global pStr
    global players
    string = entry.get()
    string2 = entry2.get()
    string3 = entry3.get()
    string4 = entry4.get()
    pStr[0] = string.split()
    pStr[1] = string2.split()
    pStr[2] = string3.split()
    pStr[3] = string4.split()
    for x in range(4):
        if len(pStr[x]) >= 3:
            players.append(player(pStr[x][0], pStr[x][1], 1500*scale, None, locations[0], pStr[x][2]))
    tk.update()
    formTk.quit()

nameInp = Label(formTk, text="Enter Players (format: \"(name) (icon) (color)\")", font=("Courier 10 bold"))
nameInp.pack()

entry = Entry(formTk, width=40)
entry.focus_set()
entry.pack()

entry2 = Entry(formTk, width=40)
entry2.focus_set()
entry2.pack()

entry3 = Entry(formTk, width=40)
entry3.focus_set()
entry3.pack()

entry4 = Entry(formTk, width=40)
entry4.focus_set()
entry4.pack()

ttk.Button(formTk, text="Submit", width=20, command=submitPlayers).pack(pady=20)
formTk.mainloop()

c = stock(23, "wegweogijo", "oij", 200, 180, 220, "summer", "machinery")
print("woiweogimwo")

d = dice()
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()
time.sleep(1)
d.roll()

canvas.mainloop()
