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

present = {"Je" : "ai", "Tu" : "as", "Il" : "a", "Elle" : "a", "Nous" : "avons", "Vous" : "avez", "Ils" : "ont", "Elles" : "ont"}
passeCompose = {"Je" : "ai eu", "Tu" : "as eu", "Il" : "a eu", "Elle" : "a eu", "Nous" : "avons eu", "Vous" : "avez eu", "Ils" : "ont eu", "Elles" : "ont eu"}
passeImparfait = {"Je" : "avais", "Tu" : "avais", "Il" : "avait", "Elle" : "avait", "Nous" : "avions", "Vous" : "aviez", "Ils" : "avaient", "Elles" : "avaient"}
passePlusQueParfait = {"Je" : "avais eu", "Tu" : "avais eu", "Il" : "avait eu", "Elle" : "avait eu", "Nous" : "avions eu", "Vous" : "aviez eu", "Ils" : "avaient eu", "Elles" : "avaient eu"}
futurSimple = {"Je" : "aurais", "Tu" : "auras", "Il" : "aura", "Elle" : "aura", "Nous" : "aurons", "Vous" : "aurez", "Ils" : "auront", "Elles" : "auront"}
passeSimple = {"Je" : "eus", "Tu" : "eus", "Il" : "eut", "Elle" : "eut", "Nous" : "eumes", "Vous" : "eutes", "Ils" : "eurent", "Elles" : "eurent"}
passeAnterieur = {"Je" : "eus eu", "Tu" : "eus eu", "Il" : "eut eu", "Elle" : "eut eu", "Nous" : "eumes eu", "Vous" : "eutes eu", "Ils" : "eurent eu", "Elles" : "eurent eu"}
futurAnterieur = {"Je" : "aurais eu", "Tu" : "auras eu", "Il" : "aura eu", "Elle" : "aura eu", "Nous" : "aurons eu", "Vous" : "aurez eu", "Ils" : "auront eu", "Elles" : "auront eu"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]

score = 0
for x in range(int(sys.argv[1])):
    sp.call("clear", shell=True)
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
    time.sleep(0.5)
print("Score:", str(score/int(sys.argv[1])*100) + "%")
