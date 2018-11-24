#! /usr/bin/python3

median = None
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nextnum = None

index = 0
while nextnum != "QUIT" and index < 40:
    nextnum = input("Enter the next item: ")
    if nextnum != "QUIT":
        nextnum = int(nextnum)
        data[index] = nextnum
        print(data)
        for x in range(len(data)):
            if data[x] < data[x]:
                temp = data[x]
                data[x] = data[x]
                data[x] = temp
        if len(data)%2 == 1:
            median = data[int(len(data)/2)]
        else:
            median = (data[int(len(data)/2)-1] + data[int(len(data)/2)]) / 2
        print("The median is now", median)
        index += 1
print("Maximum items")
