#! /usr/bin/python3

import random

x = ["allargando", "allarg.", "arco", "attacca", "bewegt", "calando", "broadening, becoming slower", "on a bowed string instrument, resume bowing after a pizzicato passage", "proceed without a break", "moving", "becoming slower and softer", "cedez", "comodo", "con sordino", "langsam", "largamente", "leger", "lentement", "l'istesso tempo", "massig", "yeild; hold the tempo back", "at a comfortable, easy tempo", "with mute", "slow, slowly", "broadly", "light, lightly", "slowly", "the same tempo", "moderate", "mit Ausdruck", "modere", "with expression", "at a moderate tempo", "mouvement", "tempo, motion", "pizzicato", "on a bowed string instrument, pluck the string instead of bowing", "ritenuto", "riten", "suddenly slower, held back"]

y = int(input("Enter number of terms to memorize: "))

while True:
	z = input(random.choice(x[:y]) + ": ")
