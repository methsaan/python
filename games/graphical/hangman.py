#! /usr/bin/python3

import subprocess as sp
import random
import time
import turtle



class Hangman():
    def __init__(self, spd, col):
        self.t = turtle.Pen()
        self.t.width(5)
        self.t.color(col)
        self.t.speed(spd)
    def create_man(self, strikenum):
        if strikenum == 1:
            self.t.forward(100)
        if strikenum == 2:
            self.t.backward(50)
            self.t.left(90)
            self.t.forward(100)
        if strikenum == 3:
            self.t.right(90)
            self.t.forward(50)
        if strikenum == 4:
            self.t.right(90)
            self.t.forward(15)
        if strikenum == 5:
            self.t.right(90)
            self.t.circle(10, 540)
        if strikenum == 6:
            self.t.right(90)
            self.t.forward(25)
        if strikenum == 7:
            self.t.right(45)
            self.t.forward(20)
        if strikenum == 8:
            self.t.backward(20)
            self.t.left(90)
            self.t.forward(20)
        if strikenum == 9:
            self.t.backward(20)
            self.t.right(45)
            self.t.backward(25)
            self.t.right(45)
            self.t.forward(20)
        if strikenum == 10:
            self.t.backward(20)
            self.t.left(90)
            self.t.forward(20)
        else:
            pass
word = input("Enter a word: ")
guessedword = []
for x in range(len(word)):
    guessedword.append("_")
sp.call("clear", shell=True)
guessedletters = []
strike = 0
state = []
h = Hangman(4, "black")
while True:
    guess = input("Guess a letter: ")
    if not guess in guessedletters:
        guessedletters.append(guess)
    else:
        print("Already guessed")
        continue
    if guess in word:
        for x in range(len(word)):
            if word.find(guess, x) != -1:
                guessedword[word.find(guess, x)] = guess
    else:
        strike = strike + 1
        h.create_man(strike)
    print(guessedword)
    if strike == 10:
        state.append("lost")
        break
    if not "_" in guessedword:
        state.append("won")
        break
if (state[0] == "lost"):
    h2 = Hangman(0, "red")
    for x in range(1, 11):
        h2.create_man(x)
    turtle.write("YOU LOST", move=False, align="center", font=("Courier", 75, "bold"))
else:
    h2 = Hangman(0, "green")
    for x in range(1, strike+1):
        h2.create_man(x)
    turtle.write("YOU WON", move=False, align="center", font=("Courier", 75, "bold"))
time.sleep(5)
