#! /usr/bin/python3

import random
import subprocess as sp
import time

countryFlags = {"red maple leaf, red verticle triband" : "Canadian",
        "13 red horizontal stripes, 50 stars at corner" : "American",
        "green stripe left, red stripe right, eagle" : "Mexican",
        "yellow diagnoal cross, green top and bottom, black sides" : "Jamaican",
        "white top half, red bottom half, flipped disc middle left" : "Greenlandic",
}

score = 0
numOfQuestions = int(eval(input("How many questions do you want? ")))
for x in range(numOfQuestions):
    randWord = random.choice(list(countryFlags))
    a = [True, False]
    b = random.choice(a)
    sp.call("clear", shell=True)
    if b:
        c = input(str(x+1) + ". Which flag has \"" + randWord + "\"? ")
        if c == countryFlags[randWord]:
            print("correct")
            score = score + 1
        else:
            print("not correct")
            print("answer: " + countryFlags[randWord])
    else:
        c = input(str(x+1) + ". What does the \"" + countryFlags[randWord] + "\" flag look like? ")
        if c == randWord:
            print("correct")
            score = score + 1
        else:
            print("answer: " + randWord)
    time.sleep(0.3)
print("Your score: " + str(100*(score/numOfQuestions)) + "%")
