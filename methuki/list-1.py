#! /usr/bin/python3

nameList = ["Methuki", "Methsaan", "Mohan"]
nameAge = [15,20,50]

name = input("what is your name ?")

if name == nameList[0]:
	print("Hello",nameList[0])

for x in range(0,3):
	print("Hello", nameList[x], ",you are", nameAge[x], "years old, right ?")
