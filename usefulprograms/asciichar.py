#! /usr/bin/python3

import subprocess as sp
import random

asciichar = []
hexDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']

while True:
    try:
        for x in range(1000):
            asciichar.append(eval("\"" + "\\" + "u" + random.choice(hexDigits) + random.choice(hexDigits)+ random.choice(hexDigits) + random.choice(hexDigits) + "\""))
        for x in asciichar:
            print(x, end=" ", flush=True)
    except UnicodeEncodeError:
        asciichar.append(eval("\"" + "\\" + "u" + random.choice(hexDigits) + random.choice(hexDigits)+ random.choice(hexDigits) + random.choice(hexDigits) + "\""))
        continue
