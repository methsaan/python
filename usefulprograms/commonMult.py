#! /usr/bin/python3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
commonMultCnt = 0
commonMult = []
aMult = []
for x in range(2000):
    aMult.append(a*x)
bMult = []
for x in range(2000):
    bMult.append(b*x)
cMult = []
for x in range(2000):
    cMult.append(c*x)
for x in range(2000):
    if x in aMult and x in bMult and x in cMult:
        commonMultCnt += 1
        commonMult.append(x)
    if commonMultCnt >= 5:
        break
print(commonMult)
