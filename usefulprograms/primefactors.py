#! /usr/bin/python3

number = int(input("Enter a number: "))
factors = []
i = 1
while True:
    if float(number/i) == float(int(number/i)):
        print(str(i) + " is a factor of " + str(number))
    if i > number:
        break
    i = i + 1
