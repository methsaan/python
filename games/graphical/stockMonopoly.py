#! /usr/bin/python3

import random
import time

from tkinter import *
from tkinter import ttk

tk = Tk()
canvas = Canvas(tk, width=2000, height=1000)
canvas.pack()

canvas.create_line(0, 100, 1600, 100, width=2)
canvas.create_line(0, 900, 1600, 900, width=2)
canvas.create_line(100, 0, 100, 1000, width=2)
canvas.create_line(1500, 0, 1500, 1000, width=2)
canvas.create_line(1600, 0, 1600, 1000, width=2)

for x in range(13):
    canvas.create_line(100*(x+2), 0, 100*(x+2), 100, width=2)

for x in range(13):
    canvas.create_line(100*(x+2), 900, 100*(x+2), 1000, width=2)

for x in range(7):
    canvas.create_line(0, 100*(x+2), 100, 100*(x+2), width=2)

for x in range(7):
    canvas.create_line(1500, 100*(x+2), 1600, 100*(x+2), width=2)

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
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-30, gamePos[1], gamePos[0]+30, gamePos[1]+20, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-15, gamePos[1]-15, gamePos[0]+15, gamePos[1]+15, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-18, gamePos[1]+20, gamePos[0]-12, gamePos[1]+26, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]+12, gamePos[1]+20, gamePos[0]+18, gamePos[1]+26, fill=symbolColor, outline=symbolColor))
        elif playerSymbolName == "suitcase":
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-30, gamePos[1]-20, gamePos[0]+30, gamePos[1]+20, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-40, gamePos[1]-10, gamePos[0]+40, gamePos[1]+10, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-40, gamePos[1]-20, gamePos[0]-20, gamePos[1], fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-40, gamePos[1], gamePos[0]-20, gamePos[1]+20, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]+20, gamePos[1], gamePos[0]+40, gamePos[1]+20, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]+20, gamePos[1]-20, gamePos[0]+40, gamePos[1], fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-25, gamePos[1]-30, gamePos[0]-20, gamePos[1]-20, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]+20, gamePos[1]-30, gamePos[0]+25, gamePos[1]-20, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-25, gamePos[1]-35, gamePos[0]+25, gamePos[1]-30, fill=symbolColor, outline=symbolColor))
        elif playerSymbolName == "shoe":
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0], gamePos[1]-20, gamePos[0]+30, gamePos[1]+10, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_rectangle(gamePos[0]-30, gamePos[1], gamePos[0], gamePos[1]+10, fill=symbolColor, outline=symbolColor))
            self.playerSymbol.append(canvas.create_oval(gamePos[0]-30, gamePos[1]-10, gamePos[0]+30, gamePos[1]+10, fill=symbolColor, outline=symbolColor))

class dice:
    def __init__(self):
        self.num = 0
        self.cube = [canvas.create_rectangle(1650, 100, 1750, 200, fill="white", outline="black", width=3), canvas.create_polygon(1650, 100, 1750, 100, 1800, 50, 1700, 50, fill="white", outline="black", width=3), canvas.create_polygon(1750, 100, 1800, 50, 1800, 150, 1750, 200, fill="white", outline="black", width=3)]
        self.dots = []
        for x in range(6):
            x = random.randrange(90)
            self.dots.append(canvas.create_oval(1650, 100+x, 1660, 110+x, fill="black", outline="black"))
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
        canvas.coords(self.dots[0], 1695, 145, 1705, 155)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="hidden")
        canvas.itemconfigure(self.dots[2], state="hidden")
        canvas.itemconfigure(self.dots[3], state="hidden")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __two(self):
        canvas.coords(self.dots[0], 1660, 110, 1670, 120)
        canvas.coords(self.dots[1], 1730, 180, 1740, 190)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="hidden")
        canvas.itemconfigure(self.dots[3], state="hidden")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __three(self):
        canvas.coords(self.dots[0], 1660, 110, 1670, 120)
        canvas.coords(self.dots[1], 1695, 145, 1705, 155)
        canvas.coords(self.dots[2], 1730, 180, 1740, 190)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="hidden")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __four(self):
        canvas.coords(self.dots[0], 1670, 120, 1680, 130)
        canvas.coords(self.dots[1], 1670, 170, 1680, 180)
        canvas.coords(self.dots[2], 1720, 120, 1730, 130)
        canvas.coords(self.dots[3], 1720, 170, 1730, 180)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="normal")
        canvas.itemconfigure(self.dots[4], state="hidden")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __five(self):
        canvas.coords(self.dots[0], 1670, 120, 1680, 130)
        canvas.coords(self.dots[1], 1670, 170, 1680, 180)
        canvas.coords(self.dots[2], 1720, 120, 1730, 130)
        canvas.coords(self.dots[3], 1720, 170, 1730, 180)
        canvas.coords(self.dots[4], 1695, 145, 1705, 155)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="normal")
        canvas.itemconfigure(self.dots[4], state="normal")
        canvas.itemconfigure(self.dots[5], state="hidden")
        tk.update()
    def __six(self):
        canvas.coords(self.dots[0], 1670, 120, 1680, 130)
        canvas.coords(self.dots[1], 1670, 170, 1680, 180)
        canvas.coords(self.dots[2], 1720, 120, 1730, 130)
        canvas.coords(self.dots[3], 1720, 170, 1730, 180)
        canvas.coords(self.dots[4], 1695, 120, 1705, 130)
        canvas.coords(self.dots[5], 1695, 170, 1705, 180)
        canvas.itemconfigure(self.dots[0], state="normal")
        canvas.itemconfigure(self.dots[1], state="normal")
        canvas.itemconfigure(self.dots[2], state="normal")
        canvas.itemconfigure(self.dots[3], state="normal")
        canvas.itemconfigure(self.dots[4], state="normal")
        canvas.itemconfigure(self.dots[5], state="normal")
        tk.update()

formTk = Tk()
formTk.geometry("500x800")

pStr = [[], [], [], []]
players = []
locations = []

for x in range(15):
    locations.append((1550-(x*100), 950))

for x in range(10):
    locations.append((50, 950-(x*100)))

for x in range(15):
    locations.append((50+(x*100), 50))

for x in range(10):
    locations.append((1550, 50+(x*100)))

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
            players.append(player(pStr[x][0], pStr[x][1], 1500, None, locations[0], pStr[x][2]))
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
