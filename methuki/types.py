#! /usr/bin/python3

# 10 - you are an idiot poo poo monkey face loser dude
# 20 - meh yer OK how ya doin
# 30 - YOU'RE AWESOME DUDE
# other - who are you GO AWAY!!
age = int(input("how old are you? "))
boolean1 = age == 10
boolean2 = age == 20
boolean3 = age == 30
if boolean1:
    print("you are an idiot poo poo monkey face loser dude")
elif boolean2:
    print("meh yer OK how ya doin")
elif boolean3:
    print('YOU\'RE AWESOME DUDE')
else:
    print("who are you, GO AWAY!!")
