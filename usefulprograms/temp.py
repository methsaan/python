#! /usr/bin/python3

# CEMC Practice

# Problem 1

n = int(input("Enter number of wood pieces: "))
h = [int(x) for x in input("Enter height of sides: ").split()][:n+2]
w = [int(x) for x in input("Enter width of sides: ").split()][:n+1]

area = 0

for x in range(n-1 if n <= 10000 else 10000):
    area += min(h[x], h[x+1])*w[x] + w[x]*(max(h[x], h[x+1])-min(h[x], h[x+1]))/2

print(area)

# Problem 2


