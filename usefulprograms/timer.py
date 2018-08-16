#! /usr/bin/python3

import subprocess as sp
import time
timer = int(input("How long: "))
def timeup():
    print("__________  _______                     _____ |       _____                       __  ")
    print("    |          |      |\            /| |      |      /                |        | |  \ ")
    print("    |          |      | \          / | |            /                 |        | |   \ ")
    print("    |          |      |  \        /  | |            |                 |        | |    \ ")
    print("    |          |      |   \      /   | |___         \                 |        | |___/")
    print("    |          |      |    \    /    | |             \_____            \      /  |  ")
    print("    |          |      |     \  /     | |                   \            \    /   |  ")
    print("    |       ___|___   |      \/      | |_____         _____/             \__/    |   ")
for x in range(timer):
    for x in range(55):
        print(timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer, "", timer)
    time.sleep(0.95)
    sp.call('clear', shell=True)
    time.sleep(0.05)
    timer = timer - 1
timeup()
time.sleep(0.95)
sp.call('clear', shell=True)
