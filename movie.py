#! /usr/bin/python3

## check if person is old enough to watch the movies
## in the movie list

## Get the users name so its easy to communicate
name = input ("What is your name ? " )

## Get the users age to check if he/she is old enough to watch the
## movies in the list
age = input ("Hello "  + name + ", how old are you ? ")
age_of = int(age)

## define a database list of movies for this experiment
print()
movies = { 'Witness': 'Adult', 'My Cousin Vinny': 'Adult', 'Anger Manegment': 'Adult', 'School for Scoundrels': 'All', 'Employee of the Month': 'All'}

## display the list of movies in the database
for i in movies:
    print("name: %s rating: %s" %(i, movies[i]))

## Ask for the users choise from the above displayed list
print()
fav_movie = input ("What is your favourite movie from the list above ? ")

for i in movies:
    if fav_movie == i:
        print ("Ok, boomer " + name + " so your favourite movie is " + fav_movie)
        #print(movies[i])
        #print(age)

    if age_of < 18:
        if movies[i] == "Adult":
            print ("And you " + name + " cannot watch your favourite movie " + fav_movie + " as it has a rating of " + movies[i])
