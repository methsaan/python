#! /usr/bin/python3

def double(n):
    return n*2

a = [4, 2, 5, 2, 5]
b = list(map(double, a))
print(b)
