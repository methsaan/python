#! /usr/bin/python3

print("Welcome to the remainder calculator")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
rem = int(first % second)
ans = int(first/second)
if rem == ans:
    rem = 0
print(str(int(first)) + " \u00F7 " + str(int(second)) + " = " + str(first/second) + " or " + str(ans) + " R " + str(rem))
