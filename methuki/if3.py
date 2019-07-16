#! /usr/bin/python3

wind = float(input("What is the wind speed in km/h ? "))
rain = float(input("How much rain fell in mm ? "))
sunshine = float(input("How strong is sunlight in lumins ? "))

cant_walk = wind > 3 and rain > 2 and sunshine > 1000

if cant_walk:
    print("The wind is " + str(wind) + "km/h and rain is greater than " + str(rain) + "mm and sunshine is greater than " + str(sunshine) + "lumins so you cannot walk")
