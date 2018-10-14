#! /usr/bin/python3

import random
import time

time_max = 40.00
tot_time = 0.0
print("You have 40 seconds")
while tot_time < time_max:
    time1 = time.time()
    x = input("Type something: ")
    time2 = time.time()
    timestr = str(time2-time1)
    print("You took " + timestr[0:timestr.index(".")+3] + " seconds to type")
    tot_time = tot_time + float(timestr)
    print("Time left: " + str(time_max-tot_time))
print("TIME'S UP")
