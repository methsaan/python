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

present = {"Je" : "finis", "Tu" : "finis", "Il" : "finit", "Elle" : "finit", "Nous" : "finissons", "Vous" : "finissez", "Ils" : "finissent", "Elles" : "finissent"}
passeCompose = {"Je" : "ai fini", "Tu" : "as fini", "Il" : "a fini", "Elle" : "a fini", "Nous" : "avons fini", "Vous" : "avez fini", "Ils" : "ont fini", "Elles" : "ont fini"}
passeImparfait = {"Je" : "finissais", "Tu" : "finissais", "Il" : "finissait", "Elle" : "finissait", "Nous" : "finissions", "Vous" : "finissiez", "Ils" : "finissaient", "Elles" : "finissaient"}
passePlusQueParfait = {"Je" : "avais fini", "Tu" : "avais fini", "Il" : "avait fini", "Elle" : "avait fini", "Nous" : "avions fini", "Vous" : "aviez fini", "Ils" : "avaient fini", "Elles" : "avaient fini"}
futurSimple = {"Je" : "finirai", "Tu" : "finiras", "Il" : "finira", "Elle" : "finira", "Nous" : "finirons", "Vous" : "finirez", "Ils" : "finiront", "Elles" : "finiront"}
passeSimple = {"Je" : "finis", "Tu" : "finis", "Il" : "finit", "Elle" : "finit", "Nous" : "finimes", "Vous" : "finites", "Ils" : "finirent", "Elles" : "finirent"}
passeAnterieur = {"Je" : "eus fini", "Tu" : "eus fini", "Il" : "eut fini", "Elle" : "eut fini", "Nous" : "eumes fini", "Vous" : "eutes fini", "Ils" : "eurent fini", "Elles" : "eurent fini"}
futurAnterieur = {"Je" : "aurais fini", "Tu" : "auras fini", "Il" : "aura fini", "Elle" : "aura fini", "Nous" : "aurons fini", "Vous" : "aurez fini", "Ils" : "auront fini", "Elles" : "auront fini"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]
presentCond = {"Je" : "finirais", "Tu" : "finirais", "Il" : "finirait", "Elle" : "finirait", "Nous" : "finirions", "Vous" : "finiriez", "Ils" : "finiraient", "Elles" : "finiraient"}
passeCond = {"Je" : "aurais fini", "Tu" : "aurais fini", "Il" : "aurait fini", "Elle" : "aurait fini", "Nous" : "aurions fini", "Vous" : "auriez fini", "Ils" : "auraient fini", "Elles" : "auraient fini"}
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
