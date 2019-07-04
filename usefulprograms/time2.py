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
"     |___/    ",
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
    printnumcoord(10, 2, bignum(int(str(datetime.datetime.now().hour)[0] if datetime.datetime.now().hour > 9 else 0)))
    printnumcoord(24, 2, bignum(int(str(datetime.datetime.now().hour)[1] if datetime.datetime.now().hour > 9 else str(datetime.datetime.now().hour)[0])))
    printnumcoord(38, 2, bignum(10))
    printnumcoord(52, 2, bignum(int(str(datetime.datetime.now().minute)[0] if datetime.datetime.now().minute > 9 else 0)))
    printnumcoord(66, 2, bignum(int(str(datetime.datetime.now().minute)[1] if datetime.datetime.now().minute > 9 else str(datetime.datetime.now().minute)[0])))
    printnumcoord(80, 2, bignum(10))
    printnumcoord(94, 2, bignum(int(str(datetime.datetime.now().second)[0] if datetime.datetime.now().second > 9 else 0)))
    printnumcoord(108, 2, bignum(int(str(datetime.datetime.now().second)[1] if datetime.datetime.now().second > 9 else str(datetime.datetime.now().second)[0])))
    sp.call("clear", shell=True)
