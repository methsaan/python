#! /usr/bin/python3

import subprocess as sp
import random
#from termcolor import cprint
#import sys

asciichar = []
hexDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']

while True:
    try:
        for a in hexDigits:
            for b in hexDigits:
                for c in hexDigits:
                    for d in hexDigits:
                        exec("print(\"\\u%%s%%s%%s%%s\" % (a, b, c, d), end=\"\", flush=True)")
                        print(a, b, c, d, end="\t", flush=True)
    except UnicodeEncodeError:
        continue
