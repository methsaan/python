#! /usr/bin/python3

import random
import sys
import subprocess as sp
import time

# present
# passe compose
# passe imparfait
# passe plus-que-parfait
# futur simple
# passe simple
# passe anterieur
# futur anterieur

present = {"Je" : "vais", "Tu" : "vas", "Il" : "va", "Elle" : "va", "Nous" : "allons", "Vous" : "allez", "Ils" : "vont", "Elles" : "vont"}
passeCompose = {"Je" : "ai alle", "Tu" : "as alle", "Il" : "a alle", "Elle" : "a alle", "Nous" : "avons alle", "Vous" : "avez alle", "Ils" : "ont alle", "Elles" : "ont alle"}
passeImparfait = {"Je" : "allais", "Tu" : "allais", "Il" : "allait", "Elle" : "allait", "Nous" : "allions", "Vous" : "alliez", "Ils" : "allaient", "Elles" : "allaient"}
passePlusQueParfait = {"Je" : "avais alle", "Tu" : "avais alle", "Il" : "avait alle", "Elle" : "avait alle", "Nous" : "avions alle", "Vous" : "aviez alle", "Ils" : "avaient alle", "Elles" : "avaient alle"}
futurSimple = {"Je" : "irai", "Tu" : "iras", "Il" : "ira", "Elle" : "ira", "Nous" : "irons", "Vous" : "irez", "Ils" : "iront", "Elles" : "iront"}
passeSimple = {"Je" : "allai", "Tu" : "allas", "Il" : "alla", "Elle" : "alla", "Nous" : "allames", "Vous" : "allates", "Ils" : "allerent", "Elles" : "allerent"}
passeAnterieur = {"Je" : "eus alle", "Tu" : "eus alle", "Il" : "eut alle", "Elle" : "eut alle", "Nous" : "eumes alle", "Vous" : "eutes alle", "Ils" : "eurent alle", "Elles" : "eurent alle"}
futurAnterieur = {"Je" : "aurais alle", "Tu" : "auras alle", "Il" : "aura alle", "Elle" : "aura alle", "Nous" : "aurons alle", "Vous" : "aurez alle", "Ils" : "auront alle", "Elles" : "auront alle"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]
presentCond = {"Je" : "irais", "Tu" : "irais", "Il" : "irait", "Elle" : "irait", "Nous" : "irions", "Vous" : "iriez", "Ils" : "iraient", "Elles" : "iraient"}
passeCond = {"Je" : "eusse alle", "Tu" : "eusses alle", "Il" : "eût alle", "Elle" : "eût alle", "Nous" : "eussions alle", "Vous" : "eussiez alle", "Ils" : "eussent alle", "Elles" : "eussent alle"}
conditionnel = [presentCond, passeCond]
conditionNames = ["present conditionel", "passe conditionel"]

score = 0
for x in range(int(sys.argv[1])):
    a = [True, True, True, False, False]
    sp.call("clear", shell=True)
    if random.choice(a) == True:
        randTense = random.choice(indicatif)
        name = indicatifNames[indicatif.index(randTense)]
        randSub = random.choice(list(randTense.keys()))
        conjGuess = input(str(x+1) + ". " + name + " " + randSub + ": ")
        conjAns = randTense[randSub]
        if conjGuess == conjAns:
            print("Correct")
            score += 1
        else:
            print("Answer:", conjAns)
    else:
        randTense = random.choice(conditionnel)
        name = conditionNames[conditionnel.index(randTense)]
        randSub = random.choice(list(randTense.keys()))
        conjGuess = input(str(x+1) + ". " + name + " " + randSub + ": ")
        conjAns = randTense[randSub]
        if conjGuess == conjAns:
            print("Correct")
            score += 1
        else:
            print("Answer:", conjAns)
    time.sleep(0.5)
print("Score:", str(score/int(sys.argv[1])*100) + "%")
