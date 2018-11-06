#! /usr/bin/python3

import math

print("Welcome to the calculator")
print('''Options: "+", "-", "x", "/", "%", "Hypotenuse"''')
oper = input("Enter operator: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
if oper == "+":
    print(str(first) + " + " + str(second) + " = " + str((first+second)))
elif oper == "-":
    print(str(first) + " - " + str(second) + " = " + str((first-second)))
elif oper == "x":
    print(str(first) + " x " + str(second) + " = " + str((first*second)))
elif oper == "/":
    print(str(first) + " / " + str(second) + " = " + str((first/second)))
elif oper == "%":
    print(str(first) + " % " + str(second) + " = " + str((first%second)))
elif oper == "hypotenuse":
    print("The hypotenuse is " + str(math.sqrt((first*first)+(second*second))))
else:
    print("YOU NEED TO IMPROVE ON YOUR DECISION MAKING SKILLS!")

