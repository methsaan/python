#! /usr/bin/python3

print("Welcome to the remainder calculator for quiz purposes")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
intans = int(round(first/second, 0))
rem = int(first % second)
print(str(intans) + " R" + str(rem))
