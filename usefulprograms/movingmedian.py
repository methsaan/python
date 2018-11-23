#! /usr/bin/python3

median = None
data = []
nextnum = None

while nextnum != "QUIT":
    nextnum = input("Enter the next item: ")
    if nextnum != "QUIT":
        nextnum = int(nextnum)
        data.append(nextnum)
        if len(data)%2 == 1:
            median = data[int(len(data)/2)]
        else:
            median = data[int(len(data)/2)-1] + data[int(len(data)/2)]
        print("The median is now", median)
