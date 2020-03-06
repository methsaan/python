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

present = {"Je" : "ecris", "Tu" : "ecris", "Il" : "ecrit", "Elle" : "ecrit", "Nous" : "ecrivons", "Vous" : "ecrivez", "Ils" : "ecrivent", "Elles" : "ecrivent"}
passeCompose = {"Je" : "ai ecrit", "Tu" : "as ecrit", "Il" : "a ecrit", "Elle" : "a ecrit", "Nous" : "avons ecrit", "Vous" : "avez ecrit", "Ils" : "ont ecrit", "Elles" : "ont ecrit"}
passeImparfait = {"Je" : "ecrivais", "Tu" : "ecrivais", "Il" : "ecrivait", "Elle" : "ecrivait", "Nous" : "ecrivions", "Vous" : "ecriviez", "Ils" : "ecrivaient", "Elles" : "ecrivaient"}
passePlusQueParfait = {"Je" : "avais ecrit", "Tu" : "avais ecrit", "Il" : "avait ecrit", "Elle" : "avait ecrit", "Nous" : "avions ecrit", "Vous" : "aviez ecrit", "Ils" : "avaient ecrit", "Elles" : "avaient ecrit"}
futurSimple = {"Je" : "ecrirai", "Tu" : "ecriras", "Il" : "ecrira", "Elle" : "ecrira", "Nous" : "ecrirons", "Vous" : "ecrirez", "Ils" : "ecriront", "Elles" : "ecriront"}
passeSimple = {"Je" : "ecrivis", "Tu" : "ecrivis", "Il" : "ecrivit", "Elle" : "ecrivit", "Nous" : "ecrivimes", "Vous" : "ecrivites", "Ils" : "ecrivirent", "Elles" : "ecrivirent"}
passeAnterieur = {"Je" : "eus ecrit", "Tu" : "eus ecrit", "Il" : "eut ecrit", "Elle" : "eut ecrit", "Nous" : "eumes ecrit", "Vous" : "eutes ecrit", "Ils" : "eurent ecrit", "Elles" : "eurent ecrit"}
futurAnterieur = {"Je" : "aurai ecrit", "Tu" : "auras ecrit", "Il" : "aura ecrit", "Elle" : "aura ecrit", "Nous" : "aurons ecrit", "Vous" : "aurez ecrit", "Ils" : "auront ecrit", "Elles" : "auront ecrit"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]
presentCond = {"Je" : "ecrirais", "Tu" : "ecrirais", "Il" : "ecrirait", "Elle" : "ecrirait", "Nous" : "ecririons", "Vous" : "ecririez", "Ils" : "ecriraient", "Elles" : "ecriraient"}
passeCond = {"Je" : "aurais ecrit", "Tu" : "aurais ecrit", "Il" : "aurait ecrit", "Elle" : "aurait ecrit", "Nous" : "aurions ecrit", "Vous" : "auriez ecrit", "Ils" : "auraient ecrit", "Elles" : "auraient ecrit"}
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
