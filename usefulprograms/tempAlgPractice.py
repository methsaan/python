#! /usr/bin/python3

import random
import subprocess as sp
import time

verbs = {"x^-n = " : "1/x^n",
        "(x^m)^n = " : "x^(mn)",
        "x^m(x^n) = " : "x^(m+n)",
        "x^m/x^n = " : "x^(m-n)",
        "(xy)^m = " : "x^m(y^m)",
        "(x/y)^m = " : "x^m/y^m",
        "1/x^n = " : "x^-n",
        "x^(mn) = " : "(x^m)^n",
        "x^(m+n) = " : "x^m(x^n)",
        "x^(m-n) = " : "x^m/x^n",
        "x^m(y^m) = " : "(xy)^m",
        "x^m/y^m = " : "(x/y)^m",
}

score = 0
numOfQuestions = int(eval(input("How many questions do you want? ")))
for x in range(numOfQuestions):
    randWord = random.choice(list(verbs))
    a = [True]
    b = random.choice(a)
    sp.call("clear", shell=True)
    if b:
        c = input(str(x+1) + " " + randWord)
        if c == verbs[randWord]:
            print("correct")
            score = score + 1
        else:
            print("answer: " + verbs[randWord])
    else:
        c = input(str(x+1) + ". How do you say \"" + verbs[randWord] + "\" in French? ")
        if c == randWord:
            print("correct")
            score = score + 1
        else:
            print("answer: " + randWord)
    time.sleep(0.3)
print("Your score: " + str(100*(score/numOfQuestions)) + "%")
