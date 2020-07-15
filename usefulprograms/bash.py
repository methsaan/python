#! /usr/bin/python3

import subprocess as sp
import time

history = []
history2 = []
cnt = 0
while True:
    x = input("Enter a bash command: ")
    cnt = cnt + 1
    if x != "bash.py-history" and x != "bash.py-clear-history":
        history2.append(x)
        history.append(str(cnt))
    if x == "bash.py-history":
        for x in range(len(history2)):
            print(history[x], "", history2[x])
    elif x[0:21] == "bash.py-clear-history":
        print("Enter range beginning: ", end="", flush=True)
        a = int(input())
        print("Enter range end: ", end="", flush=True)
        b = int(input())
        del history2[a:b]
        history = history[:len(history2)]
        cnt -= b - a
        print("DELETING RANGE ", end="", flush=True)
        for i in range(10):
            print(".", end="", flush=True)
            time.sleep(0.03)
        print(" [DONE]")
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
