#! /usr/bin/python3

median = None
data = []
datastr = ""
nextnum = None
index = 0
def sort(l):
    l.append(12345)
    for x in range(len(l)-1):
        for y in range(1, len(l)):
            if l[x] < l[y]:
                temp = l[x]
                l[x] = l[y]
                l[y] = temp
    del l[-1]
while nextnum != "QUIT" and index < 40:
    if index > 1:
        nextnum = input("Enter the next item: ")
    else:
        nextnum = 2147483648
    if nextnum != "QUIT":
        nextnum = int(nextnum)
        data.append(nextnum)
        if len(data) > 1:
            sort(data)
        datastr = data[:-1]
        datastr = datastr[1:]
        datastr = str(datastr)
        if index > 1:
            print(datastr)
        if len(data)%2 == 1:
            median = data[int(len(data)/2)]
        else:
            median = (data[int(len(data)/2)-1] + data[int(len(data)/2)]) / 2
        if index > 1:
            print("The median is now", median)
        index += 1
    else:
        quit()
print("Maximum items")
