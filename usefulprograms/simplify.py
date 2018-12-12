#! /usr/bin/python3

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

numfactors = []
denfactors = []

for x in range(1, num):
    if num/x == int(num/x):
        numfactors.append(num/x)
if numfactors[len(numfactors)-1] != 1.0:
    numfactors.append(1.0)
for x in range(1, den):
    if den/x == int(den/x):
        denfactors.append(den/x)
if denfactors[len(denfactors)-1] != 1.0:
    denfactors.append(1.0)
stat = 0
for x in range(0, len(denfactors)):
    for y in range(0, len(numfactors)):
        if numfactors[y] == denfactors[x]:
            gcf = denfactors[x]
            stat = 1
            break
    if stat == 1:
        break
simplestnum = int(num/gcf)
simplestden = int(den/gcf)
print("Simplest terms:", simplestnum, "/", simplestden)
