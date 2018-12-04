#! /usr/bin/python3

def isPrime(number):
    factors = []
    x = 1
    while True:
        if float(number/x) == float(int(number/x)):
            factors.append(x)
        if x > number:
            break
        x = x + 1
    if len(factors) <= 2:
        return True
    else:
        return False
number = int(input("Enter a number: "))
i = 1
print("Prime factors: ", end="", flush=True)
while True:
    if float(number/i) == float(int(number/i)) and isPrime(i):
        print(i, "", end="", flush=True)
    if i > number:
        break
    i = i + 1
print()
