#! /usr/bin/python3

import random
import subprocess as sp
import time

countryFlags = {"red background, big yellow star, 4 small stars forming semi-circle on the right" : "China",
        "orange, white and green horizontal stripes, navy blue 24-spoke wheel at center" : "India",
        "thirteen red and yellow horizontal stripes, blue box with 50 stars at top left corner" : "United States of America",
        "top half red, bottom half white" : "Indonesia",
        "green background, yellow rhombus center, \"Ordum e Progresso\" band and 27 stars at center" : "Brazil",
        "vertical white stripe at left, green background with white slanted moon and star" : "Pakistan",
        "green, white, green triband" : "Nigeria",
        "green background, red circle middle left" : "Bangladesh",
        "horizontal white, blue, red" : "Russia",
        "white background, red circle at center" : "Japan",
        "vertical green, white, red, golden eagle emblem at center" : "Mexico",
        "horizontal green, yellow, red, blue disk with yellow star in th middle" : "Ethiopia",
        "horizontal blue, red, white equilateral triangle on the left" : "Philippines",
        "horizontal red, white, black, golden egyptian eagle in the middle" : "Egypt",
	"red background, yellow star in the middle" : "Vietnam",
        "sky blue background, yellow star upper left, diagonal red stripe with yellow fimbriation" : "Democratic Republic of the Congo",
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
