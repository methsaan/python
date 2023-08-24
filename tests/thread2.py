#! /usr/bin/python3

# threading module
import threading
import time

done = False
cnt = 0

def countTime():
    global cnt
    while not done:
        time.sleep(1)
        cnt += 1
    return cnt

# create thread
t = threading.Thread(target=countTime)
# run thread
t.start()

x = input("Press enter: ")
done = True
print("Seconds passed:", cnt)
