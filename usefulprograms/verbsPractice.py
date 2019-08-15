#! /usr/bin/python3

import random
import subprocess as sp
import time

verbs = {"suivre" : "to follow",
        "oublier" : "to forget",
        "geler" : "to freeze",
        "grossir" : "to gain weight",
        "lever" : "to get up",
        "donner" : "to give",
        "rendre" : "to give back",
        "aller" : "to go",
        "retourner" : "to go back",
        "descendre" : "to go down",
        "sortir" : "to go out",
        "monter" : "to go up",
        "grandir" : "to grow up",
        "arriver" : "to happen",
        "detester" : "to hate",
        "avoir" : "to have",
        "chauffer" : "to heat",
        "esperer" : "to hope",
        "faire mal" : "to hurt",
        "identifier" : "to identify",
        "renseigner" : "to inform",
        "falloir" : "to need to",
        "embrasser" : "to kiss",
        "connaitre" : "to know something",
        "savoir" : "to know a fact",
        "apprendre" : "to learn",
        "partir" : "to leave",
        "preter" : "to lend",
        "aimer" : "to like or to love",
        "ecouter" : "to listen",
        "regarder" : "to look at",
        "chercher" : "to look for",
        "donner sur" : "to look onto",
        "perdre" : "to lose",
        "maigrir" : "to lose weight",
        "adorer" : "to love",
        "baisser" : "to lower",
        "marquer" : "to mark",
        "recontrer" : "to meet",
        "tromper" : "to be mistaken",
        "melanger" : "to mix",
        "obier" : "to obey",
        "observer" : "observe",
        "obtenir" : "to obtain",
        "offrir" : "to offer",
        "ouvrir" : "to open",
        "devoir" : "to owe",
        "peindre" : "to paint",
        "passer" : "to pass by",
        "payer" : "to pay",
        "permettre" : "to permit",
        "telephoner" : "to phone",
        "jouer" : "to play",
        "polluer" : "to pollute",
        "preferer" : "to prefer",
        "preparer" : "to prepare",
        "presenter" : "to present",
        "produire" : "to produce",
        "promettre" : "to promise",
        "punir" : "to punish",
        "pousser" : "to push",
        "mettre" : "to put",
        "pleuvoir" : "to rain",
        "lire" : "to read",
        "reconnaitre" : "to recognize",
        "refuser" : "to refuse",
        "regretter" : "to regret",
        "rappeler" : "to remember",
        "louer" : "to rent",
        "repeter" : "to repeat",
        "exiger" : "to require",
        "reserver" : "to reserve",
        "habiter" : "to reside",
        "reposer" : "to rest",
        "rouler" : "to roll",
        "economiser" : "to save",
        "dire" : "to say",
        "voir" : "to see",
        "sembler" : "to seem",
        "vendre" : "to sell",
        "envoyer" : "to send",
        "separer" : "to separate",
        "servir" : "to serve",
        "partager" : "to share",
        "raser" : "to shave",
        "montrer" : "to show",
        "asseoir" : "to sit down",
        "dormir" : "to sleep",
        "trier" : "to sort",
        "parler" : "to speak or to talk",
        "epeler" : "to spell",
        "espionner" : "to spy",
        "commencer" : "to start",
        "rester" : "to stay",
        "voler" : "to steal",
        "etudier" : "to study",
        "abonner" : "to subscribe",
        "reussir" : "to succeed",
        "suggerer" : "to suggest",
        "nager" : "to swim",
        "prendre" : "to take",
        "promener" : "to take a walk",
        "soigner" : "to take care",
        "raconter" : "to tell",
        "penser" : "to think",
        "menacer" : "to threaten",
        "jeter" : "to throw",
        "tracer" : "to trace",
        "voyager" : "to travel",
        "tourner" : "to turn",
        "enteindre" : "to turn off",
        "allumer" : "to turn on",
        "comprendre" : "to understand",
        "entendre" : "to wait",
        "reveiller" : "to wake up",
        "marcher" : "to walk",
        "promener" : "to walk around",
        "vouloir" : "to want",
        "laver" : "to wash",
        "regarder" : "to watch",
        "porter" : "to wear",
        "essuyer" : "to wipe",
        "inquieter" : "to worry",
        "ecrire" : "to write",
        "crier" : "to yell"
}

score = 0
numOfQuestions = int(eval(input("How many questions do you want? ")))
for x in range(numOfQuestions):
    randWord = random.choice(list(verbs))
    a = [True, False]
    b = random.choice(a)
    sp.call("clear", shell=True)
    if b:
        c = input(str(x+1) + ". How do you say \"" + randWord + "\" in English? ")
        if c == verbs[randWord]:
            print("correct")
            score = score + 1
        else:
            print("not correct")
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
