#! /usr/bin/python3

import subprocess as sp
import random
from termcolor import cprint
import sys

asciichar = []
hexDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']

y = 0
while True:
    try:
        i = y
        for x in range(10):
            asciichar.append(eval("\"" + "\\" + "u" + random.choice(hexDigits) + random.choice(hexDigits)+ random.choice(hexDigits) + random.choice(hexDigits) + "\""))
            y = y + 1
        while i <= len(asciichar)-1:
            print(asciichar[i], end=" ", flush=True)
            i = i + 1
        if y > 1000:
            break
    except UnicodeEncodeError:
        continue
