#! /usr/bin/python3

import subprocess as sp

history = []
while True:
    x = input("Enter a bash command: ")
    history.append(x)
    if x[0:7] == "python-":
        inputs = list(map(str, x.split()))
        inputstr = ''
        for c in inputs:
            inputstr += c + " "
        inputstr = inputstr[7:]
        inputstr = inputstr[:-1]
        exec(str(inputstr))
    else:
        sp.call(x, shell=True)
