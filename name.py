#! /usr/bin/python3

NAME = input ("What is your name ? ")
DAY = input("Hello " + NAME + ", rate your day from 1 - 10 ? ")

if DAY == "1":
    print("Your day was bleh")
elif DAY == "2":
    print("Your day was meh")
elif DAY == "3":
    print("Your day was mmmm")
elif DAY == "4":
    print("Your day was ahh")
elif DAY == "5":
    print("Your day was right")
elif DAY == "6":
    print("Your day was ok")
elif DAY == "7":
    print("Your day was nice")
elif DAY == "8":
    print("Your day was good")
elif DAY == "9":
    print("Your day was great")
elif DAY == "10":
    print("Your day was fantastic")
else:
    print("You can't type a number between 1 and 10 ??? ... great ...")
