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

present = {"Je" : "sers", "Tu" : "sers", "Il" : "sert", "Elle" : "sert", "Nous" : "servons", "Vous" : "servez", "Ils" : "servent", "Elles" : "servent"}
passeCompose = {"Je" : "ai servi", "Tu" : "as servi", "Il" : "a servi", "Elle" : "a servi", "Nous" : "avons servi", "Vous" : "avez servi", "Ils" : "ont servi", "Elles" : "ont servi"}
passeImparfait = {"Je" : "servais", "Tu" : "servais", "Il" : "servait", "Elle" : "servait", "Nous" : "servions", "Vous" : "serviez", "Ils" : "servaient", "Elles" : "servaient"}
passePlusQueParfait = {"Je" : "avais servi", "Tu" : "avais servi", "Il" : "avait servi", "Elle" : "avait servi", "Nous" : "avions servi", "Vous" : "aviez servi", "Ils" : "avaient servi", "Elles" : "avaient servi"}
futurSimple = {"Je" : "servirai", "Tu" : "serviras", "Il" : "servira", "Elle" : "servira", "Nous" : "servirons", "Vous" : "servirez", "Ils" : "serviront", "Elles" : "serviront"}
passeSimple = {"Je" : "servis", "Tu" : "servis", "Il" : "servit", "Elle" : "servit", "Nous" : "servimes", "Vous" : "servites", "Ils" : "servirent", "Elles" : "servirent"}
passeAnterieur = {"Je" : "eus servi", "Tu" : "eus servi", "Il" : "eut servi", "Elle" : "eut servi", "Nous" : "eumes servi", "Vous" : "eutes servi", "Ils" : "eurent servi", "Elles" : "eurent servi"}
futurAnterieur = {"Je" : "aurai servi", "Tu" : "auras servi", "Il" : "aura servi", "Elle" : "aura servi", "Nous" : "aurons servi", "Vous" : "aurez servi", "Ils" : "auront servi", "Elles" : "auront servi"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]
presentCond = {"Je" : "servirais", "Tu" : "servirais", "Il" : "servirait", "Elle" : "servirait", "Nous" : "servirions", "Vous" : "serviriez", "Ils" : "serviraient", "Elles" : "serviraient"}
passeCond = {"Je" : "eusse servi", "Tu" : "eusses servi", "Il" : "eût servi", "Elle" : "eût servi", "Nous" : "eussions servi", "Vous" : "eussiez servi", "Ils" : "eussent servi", "Elles" : "eussent servi"}
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
