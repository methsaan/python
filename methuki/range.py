#! /usr/bin/python3 

# create boolean list
# create string list
# print boolean list elements using range function and side by side
# print string list without range on each line

boolean1 = [True,False,True,False,False]
strlist = ["QWERT", "qwert", "wert", "erty", "rtyu", "tyuii", "yuio"]
for k in range(len(boolean1)):
    print(boolean1[k], end=" ", flush=True)
print()
for m in strlist:
    print(m)
F-
