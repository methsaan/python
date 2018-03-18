#! /usr/bin/python3

import math

print("Welcome to the calculator")
oper = input("Enter operator: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
if oper == "add":
    print(str(first) + " + " + str(second) + " = " + str((first+second)))
elif oper == "subtract":
    print(str(first) + " - " + str(second) + " = " + str((first-second)))
elif oper == "multiplication":
    print(str(first) + " x " + str(second) + " = " + str((first*second)))
elif oper == "division":
    print(str(first) + " / " + str(second) + " = " + str((first/second)))
elif oper == "modulus":
    print(str(first) + " % " + str(second) + " = " + str((first%second)))
elif oper == "hypotenuse":
    print("The hypotenuse is " + str(math.sqrt((first*first)+(second*second))))
else:
    print("YOU NEED TO IMPROVE ON YOUR DECISION MAKING SKILLS!")

