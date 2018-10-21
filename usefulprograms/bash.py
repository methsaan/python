#! /usr/bin/python3

import subprocess as sp

while True:
    x = input("Enter a bash command: ")
    if x[0:7] == "PYTHON-":
        inputs = list(map(str, x.split()))
        print(inputs)
        eval(x[7:len(x)])
    else:
        sp.call(x, shell=True)
