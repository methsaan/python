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

present = {"Je" : "joue", "Tu" : "joues", "Il" : "joue", "Elle" : "joue", "Nous" : "jouons", "Vous" : "jouez", "Ils" : "jouent", "Elles" : "jouent"}
passeCompose = {"Je" : "ai joue", "Tu" : "as joue", "Il" : "a joue", "Elle" : "a joue", "Nous" : "avons joue", "Vous" : "avez joue", "Ils" : "ont joue", "Elles" : "ont joue"}
passeImparfait = {"Je" : "jouais", "Tu" : "jouais", "Il" : "jouait", "Elle" : "jouait", "Nous" : "jouions", "Vous" : "jouiez", "Ils" : "jouaient", "Elles" : "jouaient"}
passePlusQueParfait = {"Je" : "avais joue", "Tu" : "avais joue", "Il" : "avait joue", "Elle" : "avait joue", "Nous" : "avions joue", "Vous" : "aviez joue", "Ils" : "avaient joue", "Elles" : "avaient joue"}
futurSimple = {"Je" : "jouerai", "Tu" : "joueras", "Il" : "jouera", "Elle" : "jouera", "Nous" : "jouerons", "Vous" : "jouerez", "Ils" : "joueront", "Elles" : "joueront"}
passeSimple = {"Je" : "jouai", "Tu" : "jouas", "Il" : "joua", "Elle" : "joua", "Nous" : "jouames", "Vous" : "jouates", "Ils" : "jouerent", "Elles" : "jouerent"}
passeAnterieur = {"Je" : "eus joue", "Tu" : "eus joue", "Il" : "eut joue", "Elle" : "eut joue", "Nous" : "eumes joue", "Vous" : "eutes joue", "Ils" : "eurent joue", "Elles" : "eurent joue"}
futurAnterieur = {"Je" : "aurai joue", "Tu" : "auras joue", "Il" : "aura joue", "Elle" : "aura joue", "Nous" : "aurons joue", "Vous" : "aurez joue", "Ils" : "auront joue", "Elles" : "auront joue"}
indicatif = [present, passeCompose, passeImparfait, passePlusQueParfait, futurSimple, passeSimple, passeAnterieur, futurAnterieur]
indicatifNames = ["present", "passe compose", "passe imparfait", "passe plus-que-parfait", "futur simple", "passe simple", "passe anterieur", "futur anterieur"]
presentCond = {"Je" : "jouerais", "Tu" : "jouerais", "Il" : "jouerait", "Elle" : "jouerait", "Nous" : "jouerions", "Vous" : "joueriez", "Ils" : "joueraient", "Elles" : "joueraient"}
passeCond = {"Je" : "aurais joue", "Tu" : "aurais joue", "Il" : "aurait joue", "Elle" : "aurait joue", "Nous" : "aurions joue", "Vous" : "auriez joue", "Ils" : "auraient joue", "Elles" : "auraient joue"}
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
