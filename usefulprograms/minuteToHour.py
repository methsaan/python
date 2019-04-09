#! /usr/bin/python3

minutes = int(input("Enter number of minutes: "))
hours = "%s:%2d" % (str(minutes//60), minutes%60)

print(hours)
