#! /usr/bin/python3

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

answer = str(dividend//divisor) + (("R" + str(dividend%divisor)) if dividend%divisor != 0 else "")

print(answer)
