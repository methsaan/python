#! /usr/bin/python3

import subprocess as sp

history = []
history2 = []
historymap = {}
cnt = 0
while True:
    x = input("Enter a bash command: ")
    cnt = cnt + 1
    history2.append(x)
    history.append(str(cnt))
    history.append(x)
    if x == "bash.py-history":
        for x in range(len(history2)):
            print(x, "", history2[x])
    elif x[0:21] == "bash.py-clear_history":
        historymap = dict(zip(history[::2], history[1::2]))
        print("Enter range beginning: ", end="", flush=True)
        x = int(input())
        print("Enter range end: ", end="", flush=True)
        y = int(input())
        for i in range(x, y):
            del history2[i]
            del history[i]
        print("history", history)
        print("history2", history2)
        print("historymap", historymap)
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
