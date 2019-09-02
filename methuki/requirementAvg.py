#! /usr/bin/python3

def sum2(*nums):
    ans = 0
    for x in range(len(nums)):
        ans += nums[x]
    return ans

f = open("dayTracker", "r")

req = []
for line in list(f)[1:]:
    words = line.split()
    req.append(words[3][2])
print(str(int(eval("sum2(" + ", ".join(req) + ")"))/(5*len(req))*100) + "% of requirements are met on average.")
