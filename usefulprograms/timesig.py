#! /usr/bin/python3

import random
import sys

duple = ["2/2", "2/4", "2/8", "6/4", "6/8", "6/16"]
triple = ["3/2", "3/4", "3/8", "9/4", "9/8", "9/16"]
quadruple = ["4/2", "4/4", "4/8", "12/4", "12/8", "12/16"]
simple = ["2/2", "2/4", "2/8", "3/2", "3/4", "3/8", "4/2", "4/4", "4/8"]
compound = ["6/4", "6/8", "6/16", "9/4", "9/8", "9/16", "12/4", "12/8", "12/16"]
times = ["2/2", "2/4", "2/8", "3/2", "3/4", "3/8", "4/2", "4/4", "4/8", "6/4", "6/8", "6/16", "9/4", "9/8", "9/16", "12/4", "12/8", "12/16"]

for x in range(int(sys.argv[1])):
    randtimes = random.choice(times)
    print("Time signature type of:", randtimes)
    if 
