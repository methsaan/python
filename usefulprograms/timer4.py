#! /usr/bin/python3

import time
import subprocess as sp

def timeup():
    print("__________  _______                     _____ |       _____                       __  ")
    print("    |          |      |\            /| |      |      /                |        | |  \ ")
    print("    |          |      | \          / | |            /                 |        | |   \ ")
    print("    |          |      |  \        /  | |            |                 |        | |    \ ")
    print("    |          |      |   \      /   | |___         \                 |        | |___/")
    print("    |          |      |    \    /    | |             \_____            \      /  |  ")
    print("    |          |      |     \  /     | |                   \            \    /   |  ")
    print("    |       ___|___   |      \/      | |_____         _____/             \__/    |   ")

def print_char(x, y, char):
    print("\033["+str(y)+";"+str(x)+"H"+char)

def bignum(smallnum):
    numbers = [["   --------   ",
        "  /        \\  ",
        " /          \\ ",
        " |           | ",
        " |           | ",
        " \\         /  ",
        "  \\       /   ",
        "   \\-----/    ", 
        "               "],
        ["       /|     ",
        "      / |     ",
        "     /  |     ",
        "        |     ",
        "        |     ",
        "        |     ",
        "        |     ",
        "    ____|____ ",
        "              "],
        ["      ____    ",
        "     /    \\  ",
        "     |    |   ",
        "         /    ",
        "        /     ",
        "       /      ",
        "      /       ",
        "     /_____   ",
        "              "],
        ["     ______   ",
        "           /  ",
        "          /   ",
        "         /_   ",
        "           \\ ",
        "           |  ",
        "           /  ",
        "     \\___/   ",
        "              "],
        ["        /|    ",
        "       / |    ",
        "      /  |    ",
        "     /   |    ",
        "    /____|___ ",
        "         |    ",
        "         |    ",
        "         |    ",
        "              "],
        ["       ____   ",
        "      /       ",
        "     /        ",
        "    /_____    ",
        "          \\  ",
        "          |   ",
        "         /    ",
        "     ___/     ",
        "              "],
        ["       ____   ",
        "      /       ",
        "     /        ",
        "    /_____    ",
        "   /      \\  ",
        "   \\      |  ",
        "    \\    /   ",
        "     \\__/    ",
        "              "],
        ["   ________   ",
        "          /   ",
        "         /    ",
        "        /     ",
        "     __/__    ",
        "      /       ",
        "     /        ",
        "    /         ",
        "              "],
        ["     _____    ",
        "    /     \\  ",
        "   /       \\ ",
        "   \\      /  ",
        "    \\____/   ",
        "    /     \\  ",
        "    \\    /   ",
        "     \\__/    ",
        "              "],
        ["      ______  ",
        "     /      \ ",
        "     |      | ",
        "     |      | ",
        "     \\_____/ ",
        "            | ",
        "           /  ",
        "       ___/   ",
        "              "],
        ["              ",
        "      _       ",
        "     |_|      ",
        "              ",
        "              ",
        "      _       ",
        "     |_|      ",
        "              ",
        "              "]]
    return numbers[smallnum]

def printnumcoord(x, y, stringarr):
    for i in range(8):
        print_char(x, y+i, stringarr[i])
timer = input("Enter number of seconds: ")
timerlist = [int(timer[0]), int(timer[1]), int(timer[3]), int(timer[4]), int(timer[6]), int(timer[7])]
while timerlist != [0, 0, 0, 0, 0, 0]:
        printnumcoord(30, 14, bignum(timerlist[0]))
        printnumcoord(44, 14, bignum(timerlist[1]))
        printnumcoord(58, 14, bignum(10))
        printnumcoord(72, 14, bignum(timerlist[2]))
        printnumcoord(86, 14, bignum(timerlist[3]))
        printnumcoord(100, 14, bignum(10))
        printnumcoord(114, 14, bignum(timerlist[4]))
        printnumcoord(128, 14, bignum(timerlist[5]))
        time.sleep(1)
        timerlist[5] -= 1
        if timerlist[5] < 0:
            timerlist[5] = 9
            timerlist[4] -= 1
            if timerlist[4] < 0:
                timerlist[4] = 5
                timerlist[3] -= 1
                if timerlist[3] < 0:
                    timerlist[3] = 9
                    timerlist[2] -= 1
                    if timerlist[2] < 0:
                        timerlist[2] = 5
                        timerlist[1] -= 1
                        if timerlist[1] < 0:
                            timerlist[1] = 9
                            timerlist[0] -= 1
        sp.call("clear", shell=True)
timeup()
