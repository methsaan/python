#! /usr/bin/python3

import psycopg2
import random

# create a random number between 1 and 125
randomIndex = random.randrange(1,125)

DB="french_verbs"
USER="methsaan"
PASS="welcome"
IP="192.168.2.225"
PORT="5432"

#usrAnswer = input("What is " + str(randomIndex) + "? ")
#print(usrAnswer)

conn = psycopg2.connect(database=str(DB), user=str(USER), password=str(PASS), host=str(IP), port=str(PORT))

cur = conn.cursor()

# select the values for the index chosen by random
cur.execute("SELECT english,french from verb where id = " + str(randomIndex) + ";")

rows = cur.fetchall()
for row in rows:
   english_value=row[1]
   french_value=row[0]

userAnswer = input("How do you say \"" + english_value + "\" in french? ")
if userAnswer == french_value:
    print("correct")
else:
    print("not correct")
    print("Answer:", french_value)
conn.commit()
conn.close()
