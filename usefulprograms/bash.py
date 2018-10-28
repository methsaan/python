#! /usr/bin/python3

import subprocess as sp
import tkinter

history = []
historymap = {}
while True:
    x = input("Enter a bash command: ")
    history.append(x)
    if x == "bash.py-history":
        for x in range(len(history)):
            print(x, "", history[x])
            historymap = dict(str(x), history[x])
    elif x[0:21] == "bash.py-clear_history":
        print(historymap["12"])
    elif x[0:12] == "python-exec-":
        inputs = list(map(str, x.split()))
        inputstr = ''
        for c in inputs:
            inputstr += c + " "
        inputstr = inputstr[12:]
        inputstr = inputstr[:-1]
        exec(inputstr)
    elif x[0:12] == "python-eval-":
        inputs = list(map(str, x.split()))
        inputstr = ''
        for c in inputs:
            inputstr += c + " "
        inputstr = inputstr[12:]
        inputstr = inputstr[:-1]
        print(eval(inputstr))
    else:
        sp.call(x, shell=True)
