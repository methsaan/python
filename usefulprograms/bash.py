#! /usr/bin/python3

import subprocess as sp
from itertools import izip

history = []
history2 = []
historymap = {}
cnt = 0
while True:
    x = input("Enter a bash command: ")
    cnt = cnt + 1
    history2.append(x)
    history.append(cnt)
    history.append(x)
    if x == "bash.py-history":
        for x in range(len(history2)):
            print(x, "", history2[x])
    elif x[0:21] == "bash.py-clear_history":
        historymap = dict(zip(history[::2], a[1::2]))
        print("Enter commands to remove from history: ", end="", flush=True)
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
