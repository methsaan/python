#! /usr/bin/python3

import subprocess as sp
import time
month = []
day = []
schedule = []
numOfReq = []
reason = []

month.append(input("Month: (q to show schedule) "))
if month[0] == "q":
    quit()
day.append(input("Date: "))
schedule.append(input("Fwor/Fwr/perfect/PERFECT: "))
print("Requirements: PA, PP, D, MT, ST")
numOfReq.append(input("Number of requirements met /4: ") + "/4")
reason.append(input("Reason / N/A: "))
open("dayTracker", "a").write(str(month));
open("dayTracker", "a").write("\t\t");
open("dayTracker", "a").write(str(day));
open("dayTracker", "a").write("\t");
open("dayTracker", "a").write(str(schedule));
open("dayTracker", "a").write("\t\t\t\t");
open("dayTracker", "a").write(str(numOfReq));
open("dayTracker", "a").write("\t\t\t");
open("dayTracker", "a").write(str(reason));
open("dayTracker", "a").write("\n");
if input("Type 'd' and enter to see your progress\n") == "d":
    for x in range(len(day)):
        print(open("dayTracker").read())
    x = input("Type 's' to stop showing: ")
    if x == "s":
        sp.call("clear", shell=True)
