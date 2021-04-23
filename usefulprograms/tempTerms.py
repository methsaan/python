#! /usr/bin/python3

import random
import time
import subprocess as sp

a = ["allargando", "allarg", "arco", "attacca", "bewegt", "calando", "cedez", "comodo", "con sordino", "fp", "fortepiano", "langsam", "largamente", "leger", "lentement", "l'istesso tempo", "massig", "mit ausdruck", "modere", "mouvement", "pizzicato", "ritenuto", "riten", "schnell", "sehr", "sfz", "stringendo", "vite"]
b = ["broadening, becoming slower", "broadening becoming slower", "on a bowed string instrument, resume bowing after a pizzicato passage", "proceed without a break", "moving", "becoming slower and softer", "yield; hold the tempo back", "at a comfortable, easy tempo", "with mute", "loud, then suddenly soft", "fortepiano", "langsam", "largamente", "leger", "lentement", "l'istesso tempo", "massig", "mit ausdruck", "modere", "mouvement", "pizzicato", "ritenuto", "riten", "schnell", "sehr", "sfz", "stringendo", "vite"]

y = int(input("Enter number of terms to memorize: "))

while True:
    if random.choice([True, False]):
        r = random.randrange(0, y)
        z = input(a[r] + ": ")
        if z == b[r]:
            print("Correct")
        else:
            print("Incorrect")
            print(b[r])
    else:
        r = random.randrange(0, y)
        z = input(b[r] + ": ")
        if z == a[r]:
            print("Correct")
        else:
            print("Incorrect")
            print(a[r])
    time.sleep(2)
    sp.call("clear")
