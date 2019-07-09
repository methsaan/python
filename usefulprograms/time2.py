#! /usr/bin/python3

import time
import datetime
import subprocess as sp

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
        "     /        "
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
while True:
        printnumcoord(30, 14, bignum(int(str(datetime.datetime.now().hour)[0] if datetime.datetime.now().hour > 9 else 0)))
        printnumcoord(44, 14, bignum(int(str(datetime.datetime.now().hour)[1] if datetime.datetime.now().hour > 9 else str(datetime.datetime.now().hour)[0])))
        printnumcoord(58, 14, bignum(10))
        printnumcoord(72, 14, bignum(int(str(datetime.datetime.now().minute)[0] if datetime.datetime.now().minute > 9 else 0)))
        printnumcoord(86, 14, bignum(int(str(datetime.datetime.now().minute)[1] if datetime.datetime.now().minute > 9 else str(datetime.datetime.now().minute)[0])))
        printnumcoord(100, 14, bignum(10))
        printnumcoord(114, 14, bignum(int(str(datetime.datetime.now().second)[0] if datetime.datetime.now().second > 9 else 0)))
        printnumcoord(128, 14, bignum(int(str(datetime.datetime.now().second)[1] if datetime.datetime.now().second > 9 else str(datetime.datetime.now().second)[0])))
        sp.call("clear", shell=True)
