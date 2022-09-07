#! /usr/bin/python3

try:
    x = input("Enter equation: ")
    y = int(input("Enter number: "))
    print("Answer: " + str(eval(x)/y))
except ZeroDivisionError:
    print("Answer: Infinity")
except (ValueError, NameError, SyntaxError):
    print("One of your numbers is not valid.") 
finally:
    print("wefoiwehfoih")
