#! /usr/bin/python3

import time

time1 = time.time()
print("Type something")
x = input()
while x[len(x)-1] != "~":
    x = input()
time2 = time.time()
timestr = str(time2-time1)
print("You took " + timestr[0:timestr.index(".")+3] + " seconds to type")
