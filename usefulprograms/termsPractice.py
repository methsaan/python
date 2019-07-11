#! /usr/bin/python3

import random
import subprocess as sp
import time

verbs = {"agitato" : "agitated",
        "dolente" : "sad",
        "giocoso" : "humorous",
        "grandioso" : "grand",
        "martellato" : "strongly accented",
        "mesto" : "mournful",
        "morendo" : "fading away",
        "pesante" : "with emphasis",
        "quindicesima alta" : "two octaves higher",
        "risoluto" : "resolute",
        "scherzando" : "playful",
        "semplice" : "simple",
        "sonore" : "sonorous",
        "sopra" : "above",
        "sostenuto" : "sustained",
        "sotto voce" : "subdued",
        "tacet" : "be silent",
        "tutti" : "a passage for the ensemble",
        "vivo" : "lively",
        "volta" : "time",
        "volti subito" : "turn the page quickly"
}

score = 0
numOfQuestions = int(input("How many questions do you want? "))
for x in range(numOfQuestions):
    randWord = random.choice(list(verbs))
    a = [True, False]
    b = random.choice(a)
    sp.call("clear", shell=True)
    if b:
        c = input("How do you say \"" + randWord + "\" in english? ")
        if c == verbs[randWord]:
            score = score + 1
            print("Correct")
        else:
            print("answer: " + verbs[randWord])
        time.sleep(1)
    else:
        c = input("What is the music term for \"" + verbs[randWord] + "\"? ")
        if c == randWord:
            score = score + 1
            print("Correct")
        else:
            print("answer: " + randWord)
        time.sleep(1)
print("Your score: " + str(100*(score/numOfQuestions)) + "%")
