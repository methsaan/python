#! /usr/bin/python3

import random

verbs = {"the socks" : "les chaussettes",
        "the pants" : "les pantalons",
        "the shirt" : "la chemise",
        "the jeans" : "les jeans",
        "the baithing suit" : "le maillot de bain",
        "the dress" : "la robe",
        "the boots" : "les bottes",
        "the sleeves" : "la manche",
        "the sweater" : "le pull",
        "the cap" : "la casquette"
}

score = 0
numOfQuestions = int(input("How many questions do you want? "))
for x in range(numOfQuestions):
    randWord = random.choice(list(verbs))
    a = [True, False]
    b = random.choice(a)
    if b:
        c = input("How do you say \"" + randWord + "\" in english? ")
        if c == verbs[randWord]:
            score = score + 1
        else:
            print("answer: " + verbs[randWord])
    else:
        c = input("How do you say \"" + verbs[randWord] + "\" in french? ")
        if c == randWord:
            score = score + 1
        else:
            print("answer: " + randWord)
print("Your score: " + str(100*(score/numOfQuestions)) + "%")
