#! /usr/bin/python3

median = None
data = []
nextnum = None

index = 0
while nextnum != "QUIT" and index < 40:
    nextnum = input("Enter the next item: ")
    if nextnum != "QUIT":
        nextnum = int(nextnum)
        data.append(nextnum)
        if len(data) > 1:
            for x in range(len(data)-1):
                tempElement = data[x]
                for y in range(len(data)-1):
                    if tempElement > data[y+1]:
                        temp = tempElement
                        data[x] = data[x+1]
                        data[x+1] = temp
        print(data)
        if len(data)%2 == 1:
            median = data[int(len(data)/2)]
        else:
            median = (data[int(len(data)/2)-1] + data[int(len(data)/2)]) / 2
        print("The median is now", median)
        index += 1
    else:
        quit()
print("Maximum items")
