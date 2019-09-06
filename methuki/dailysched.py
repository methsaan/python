#! /usr/bin/python

import sys
import subprocess as sp
import random
import datetime

breaktype = sys.argv[1]
sp.call("clear", shell=True)
sp.call("./dayTracker2.py", shell=True)
daylist = [1, 2, 3, 4, 5, 6, 0]
dayx = daylist[datetime.datetime.today().weekday()]
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
timea = datetime.datetime.now().strftime("%H:%M:%S")
if timea[0] == '1' and timea[1] == '8' and timea[3] == '2':
    fpw = open("schedfile", "w")
    fpw.write("%s\n" % dayx)
    fpw.write("%s\n" % random.randrange(2))
    fpw.write("%s\n" % random.randrange(12))
    fpw.write("%s\n" % random.randrange(2))
    studytypes = ["Geometry", "EQAO", "Algebra", "English Writing", "French Grammar", "English Language", "Sinhala Vocabulary", "Government", "Countries", "Hacking", "Human Body"]
    fpw.write("%s" % random.choice(studytypes))
    fpw.close()
fp = open("schedfile", "r")
filelines = fp.read().split("\n")
dayy = int(filelines[0])
randnum = int(filelines[1])
randday = int(filelines[2])
randnum2 = int(filelines[3])
studytype = filelines[4]
fp.close()
sp.call("./requirementAvg.py")
sp.call("git commit -a -m 'day tracker'", shell=True)
sp.call("git push", shell=True)
idx = 0
if breaktype == "free":
    idx = 2
elif breaktype == "tennis":
    idx = 0
elif breaktype == "swimming/tennis":
    idx = 3
elif breaktype == "swimming":
    idx = 1
sp.call("clear", shell=True)
print("Today is %s, %s %s, %s, %s." % (days_of_the_week[dayx], datetime.datetime.now().strftime("%B"), datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%Y"), timea))
pdbr = [["PDBR1", "PDBR2"], ["PDBR3", "PDBR4"], ["PDBR5", "PDBR6"], ["PDBR7", "PDBR8"]]
if dayy == 0:
    print("Today you are following schedule %s, FAIL%s or %s" % (("SUN1" if randnum2 == 0 else "SUN2"), randnum2+1, pdbr[idx][randnum]))
elif dayy == 6:
    print("Today you are following schedule %s, FAIL%s or %s" % (("SAT1" if randnum2 == 0 else "SAT2"), randnum2+1, pdbr[idx][randnum]))
else:
    day_array = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    print("Today you are following schedule %s, FAIL%s or %s" % (day_array[randday], randnum2+1, pdbr[idx][randnum]))
print("Study subject: %s" % studytype)
print("__________________________________________________________________________________________________________________________________________________________________________________________")
print("| REGULAR SCHEDULE     Wake up 5:30 AM      Sleep 8:40 PM         Workout:      Push ups:   3 sets of 2      Squats:   2 sets of 20     Plank: 1.5 min               |     FAIL1         |")
print("|____________________________________________________________________________________________________________________________________________________________________|___________________|")
print("|_________1_________|_________3_________|_______ 5  _______|_______SAT1_______|______SUN1______|______PDBR1______|_____PDBR3_______|_____PDBR5_____|______PDBR7______|6-12:00AM __1___   |")
print("|        PA         |        PA         |    Study + D    |(PA+Breakfast+OA)/PA|      PA       |       PA        |       PA        |      PA       |       PA        |           PA      |")
print("|   FT + Breakfast  |   FT + Breakfast  |        PA        |   C / Breakfast  |(Breakfast+OA)/FT|    Breakfast   |    Breakfast    |   Breakfast   |    Breakfast    |            D      |")
print("|      Pack         |       Pack        |       FB         |        FB        |      Python    |        OA       |    OA/Swimming  |     python    |   Swimming/OA   |2-4:00PM  __2___   |")
print("|        D          |    FB + python    |        Pack      |       OA         |       FT       |      Study      |       python    |       OA      |     python      |           ST      |")
print("|       FB          |     Breakfast     |    Breakfast     |      Study       |       D        |     python      |         D       |       FT      |       D         |           SW      |")
print("|     School        |      School       |      School      |      Lunch       |      Lunch     |        PA       |        PA       |       ST      |      PP         |4-5:00PM  __3___   |")
print("|      Lunch        |       Lunch       |      Lunch       |        D         |      Study     |        PP       |       FT        |       D       |      Lunch      |            D      |")
print("|    Study          |         D         |        HW        |        FT        |       FT       |      Lunch      |     Lunch       |     Lunch     |    Tennis       |           PA      |")
print("|       HW          |    Study + HW     |        PA        |     Study        |       SW       |     Tennis      |       python    |      FT       |                 |5-6:00PM  __4___   |")
print("|       PP          |         PP        |        FT        |        PA        |       FT       |         D       |       ST        |      PP       |      PA         |            PP     |")
print("|       PA          |        PA         |        D         |        PP        |       PA       |      Python     |       PP        |      PA       |      ST         |           Study   |")
print("|       FT          |         FT        |        PP        |      python      |      python    |        FT       |        FT       |      ST       |      FT         |6-7:00PM  __5___   |")
print("|     Dinner        |      Dinner       |      Dinner      |      Dinner      |      Dinner    |      Dinner     |     Dinner      |       D       |      SW         |           FT      |")
print("|     Sleep         |      Sleep        |      Sleep       |      Sleep       |      Sleep     |      Sleep      |      Sleep      |    Dinner     |    Dinner       |         python    |")
print("|                   |                   |                  |                  |                |                 |                 |      SW       |    Sleep        |7-11:00PM __6___   |")
print("|                   |                   |                  |                  |                |                 |                 |    Sleep      |                 |     Dinner + Sleep|")
print("|___________________|___________________|__________________|__________________|________________|_________________|_________________|_______________|_________________|___________________|_")
print("|                                                             TIMED SCHEDULE            Wake up 5:30 AM                                                               |      FAIL2         |")
print("|_____________________________________________________________________________________________________________________________________________________________________|____________________|")
print("|         2         |         4         |        6         |       SAT2       |      SUN2      |      PDBR2      |      PDBR4      |     PDBR6      |    PDBR8        |5-12:00AM  __1___   |")
print("|___________________|___________________|__________________|__________________|________________|_________________|_________________|________________|_________________|            Study   |")
print("|6:05|    PA        |6:05|    PA        |6:05|    PA       |6:05|    PA       |6:05|   PA      |5:55|    PA      |5:55|    PA      |5:55|    PA     |5:55|    PA      |             FT     |")
print("|6:20|FT + Breakfast|6:20|FT +   FB     |6:20|    D        |6:20|   Study     |6:20|FB+Breakfa.|6:10|  Breakfast |6:10| Breakfast  |6:10|  Breakfast|6:10| Breakfast  |2-4:00PM   __2___   |")
print("|6:50|    FB        |6:40|  Breakfast   |7:20|  Breakfast  |7:00| Breakfast+FT|7:10|    D      |6:25| OA/HW/ST   |6:25| FB + OA/ST |6:25| FB + OA/ST|6:25|    FB      |             D      |")
print("|7:00|    Pack      |7:10|   FB + PP    |7:50| FB  + Pack  |8:00|    FB       |8:00|   PP      |7:50|    PP      |7:50|    PP      |8:00|    D      |7:00|    D       |            PP      |")
print("|7:10|     D        |7:50|    Pack      |8:00|  School     |8:10|    PP       |9:00|_ HW / FT  |8:50|    D       |8:35|    D       |9:00|_HW + FT   |8:00|   PP       |4-5:00PM   __3___   |")
print("|8:00|   School     |8:00|   School     |2:55|  Lunch      |9:00|_  HW/ FT    |10:00|   SW     |9:50|_   PR      |8:50|_ Swimming  |11:00|  PP      |8:50|  Swimming  |            SW      |")
print("|2:55|   Lunch      |2:55|   Lunch      |3:25|    FT       |10:00|   D        |10:30|  Study   |10:50|   FT      |11:15|   FT      |11:40|  Lunch   |11:15|   FT      |            PA      |")
print("|3:25|    HW        |3:25|    SW        |4:25|   Study     |11:40|  Lunch     |11:30|   PP     |11:00|   PP      |11:35|   PP      |12:20|  Study   |12:00|  Lunch    |5-6:00PM   __4___   |")
print("|4:25|    FT        |4:25|    HW        |5:25|    HW       |12:40| Program    |12:10|   D      |12:00|   Lunch   |12:20|  Lunch    |1:20|     D     |12:40|    D      |             D      |")
print("|5:25|   Study      |5:25|    PA        |6:25|    PA       |2:00|    FT       |1:10|  Study    |12:40|   Study   |1:00| HW / Study |2:20|    FT     |1:40|   Study    |             PA     |")
print("|6:25|    PA        |5:40|   Study      |6:30|    D        |4:00|    PP       |2:10|   FT      |1:40|    D       |2:00|    D       |3:20|    PR     |2:30|   tennis   |6-7:00PM   __5___   |")
print("|6:40|    D         |6:40|  D + FT      |7:30|    PP       |5:00|    PA       |4:00|   PR      |2:10|    Tennis  |3:00|    SW      |4:20|    PP     |5:00|    FT      |          python    |")
print("|7:10|   PP         |8:00|   Dinner     |8:00|  Dinner     |5:15|  Study      |5:00|   PA      |5:00|    SW      |3:30|    FT      |5:00|    PA     |6:00|    PR      |            FT      |")
print("|8:00|   Dinner     |8:40|___SLEEP______|8:40|___SLEEP_____|6:15|    D        |5:15|   PP      |5:30|    PR      |4:30|    PP      |5:20|    SW     |7:00|    PA      |7-11:00PM  __6___   |")
print("|8:40|____SLEEP_____|                                      |7:15|  Dinner     |6:15|   SW      |6:30|    PA      |5:10|    PA      |5:50|    ST     |7:15|    D       |                    |")
print("                                                           |8:00|  Sleep      |7:15|  Dinner   |6:50|    FT      |5:30|   Study    |6:50|     D     |7:50|   Dinner   |    Dinner + Sleep  |")
print("Codes:                                                     |____|_____________|8:00|___SLEEP___|7:50|    D       |6:30|     D      |7:50|  Dinner   |8:40|___SLEEP____|____________________|")
print("                                                                                               |7:10|   Dinner   |7:30|  Dinner    |8:40|___SLEEP___|                                       ")
print("PA = Physical activity          B = Breakfast                                                  |8:10|____SLEEP___|8:20|___SLEEP____|                                                        ")
print("OA = Outdoor activity           PP = Piano practice                                                                                                                                         ")
print("PR = program\t\t\tST = Study\t\t\tFB = fold blanket\t\t\tSW = story writing")
print("FT = Free time\t\t\tHW = Homework")
print("/ = do either one\t\t\tD = duolingo")
print("+ = do both in any order\n")
print("Schedules:\n")
print("PDBR1/2: Tennis\t\t\t")
print("PDBR3/4: Swimming")
print("PDBR5/6: Free\t\t\t")
print("PDBR7/8: Tennis/Swimming")
print("REMINDERS : washroom = 30min, Fold blanket = 10min, PA 15 min, Programming/Hacking 1 hr, study 1 hrs, Breakfast = 30 min, Lunch = 40 min, Dinner = 40 min")
