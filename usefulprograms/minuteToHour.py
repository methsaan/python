#! /usr/bin/python3

minutes = int(input("Enter number of minutes: "))
hours = "%s:%s" % (str(minutes//60), str(minutes%60).zfill(2))

print(hours)
