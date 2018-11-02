#! /usr/bin/python3

import subprocess as sp
import random

sp.call("clear")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, " "]

x = 0

while True:
    print(str(random.choice(digits)), end="", flush=True)
    x = x + 1
    if x%100 == 0:
        print()
    if x == 5000:
        break
