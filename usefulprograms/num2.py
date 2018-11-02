#! /usr/bin/python3

import subprocess as sp
import random

sp.call("clear")

digits=[1,2,3,4,5,6,7,8,9,0," ",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','~','`','_','-','+','=','[',']','{','}','|','\\','/','?','.','>','<',',',' ',' ',' ',' ',' ',' ',' ',' ']

x = 0

while True:
    print(str(random.choice(digits)), end="", flush=True)
    x = x + 1
    if x%100 == 0:
        print()
    if x == 5000:
        break
