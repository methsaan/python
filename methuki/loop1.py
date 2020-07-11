#! /usr/bin/python3

movies = ["Employee of the Month", "Here Comes the Boom", "Let's Go To Prison", "Madagascar 1 ", "Chef", "Observe and Report", "School of Rock", "Anger Managment", "School for Scoundrels", "Dinner for Shmucks", "Uncle Buck", "Over the Hedge", "Heat"]

name = input ("Hi what is you name? ")
age = int(input ("Hello " + name + ", how old are you? "))

print()

for x in range(0, 12):
    print(movies[x])

print()
favMovie = input ("What is your favourite movie from this list? ")
print()

rated = [movies[0], movies[2], movies[4], movies[5], movies[8], movies[9]]
rated2 = [movies[2], movies[4], movies[5], movies[12]]
if age < 13 and favMovie in rated:
    print ("Sorry, " + name + "you are not aloud to watch movies in this list, try the kids section")
    print()
    for x in rated:
        print(x)
if age == 13 and favMovie in movies:
    print ("Sorry, " + name + "you are not aloud to watch")
    print()
    print (movies[2]) 
    print (movies[5])
    print (movies[4])
    print (movies[12])
if age > 13 and favMovie in movies:
    print("You can can watch any movie in the list!!")
    print()
else:
    print ("Movie not in the list")
