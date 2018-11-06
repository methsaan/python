#! /usr/bin/python3

import math

def equals(str1, str2):
    return str1.upper() == str2.upper()
print("Welcome to the calculator")
print('''Options: "+", "-", "x", "/", "%", "hypotenuse"''')
oper = input("Enter operator: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
if oper == "+":
    print(str(first) + " + " + str(second) + " = " + str((first+second)))
elif oper == "-":
    print(str(first) + " - " + str(second) + " = " + str((first-second)))
elif oper == "x":
    print(str(first) + " \u00D7 " + str(second) + " = " + str((first*second)))
elif oper == "/":
    print(str(first) + " \u00F7 " + str(second) + " = " + str((first/second)))
elif oper == "%":
    print(str(first) + " % " + str(second) + " = " + str((first%second)))
elif equals(oper, "hypotenuse"):
    print("The hypotenuse is " + str(math.sqrt((first*first)+(second*second))))
else:
    print("YOU NEED TO IMPROVE ON YOUR DECISION MAKING SKILLS!")

