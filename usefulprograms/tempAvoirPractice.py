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

present = {"Je" : "parle", "Tu" : "parles", "Il" : "parle", "Elle" : "parle", "Nous" : "parlons", "Vous" : "parlez", "Ils" : "parlent", "Elles" : "parlent"}
passeCompose = {"Je" : "ai parle", "Tu" : "as parle", "Il" : "a parle", "Elle" : "a parle", "Nous" : "avons parle", "Vous" : "avez parle", "Ils" : "ont parle", "Elles" : "ont parle"}
passeImparfait = {"Je" : "parlais", "Tu" : "parlais", "Il" : "parlait", "Elle" : "parlait", "Nous" : "parlions", "Vous" : "parliez", "Ils" : "parlaient", "Elles" : "parlaient"}
passePlusQueParfait = {"Je" : "avais parle", "Tu" : "avais parle", "Il" : "avait parle", "Elle" : "avait parle", "Nous" : "avions parle", "Vous" : "aviez parle", "Ils" : "avaient parle", "Elles" : "avaient parle"}
futurSimple = {"Je" : "parlerai", "Tu" : "parleras", "Il" : "parlera", "Elle" : "parlera", "Nous" : "parlerons", "Vous" : "parlerez", "Ils" : "parleront", "Elles" : "parleront"}
passeSimple = {"Je" : "parlai", "Tu" : "parlas", "Il" : "parla", "Elle" : "parla", "Nous" : "parlames", "Vous" : "parlates", "Ils" : "parlerent", "Elles" : "parlerent"}
passeAnterieur = {"Je" : "eus parle", "Tu" : "eus parle", "Il" : "eut parle", "Elle" : "eut parle", "Nous" : "eumes parle", "Vous" : "eutes parle", "Ils" : "eurent parle", "Elles" : "eurent parle"}
futurAnterieur = {"Je" : "aurais parle", "Tu" : "auras parle", "Il" : "aura parle", "Elle" : "aura parle", "Nous" : "aurons parle", "Vous" : "aurez parle", "Ils" : "auront parle", "Elles" : "auront parle"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]
presentCond = {"Je" : "parlerais", "Tu" : "parlerais", "Il" : "parlerait", "Elle" : "parlerait", "Nous" : "parlerions", "Vous" : "parleriez", "Ils" : "parleraient", "Elles" : "parleraient"}
passeCond = {"Je" : "aurais parle", "Tu" : "aurais parle", "Il" : "aurait parle", "Elle" : "aurait parle", "Nous" : "aurions parle", "Vous" : "auriez parle", "Ils" : "auraient parle", "Elles" : "auraient parle"}
conditionnel = [presentCond, passeCond]
conditionNames = ["present conditional", "passe conditional"]

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
