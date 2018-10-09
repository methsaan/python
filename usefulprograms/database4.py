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

conn = psycopg2.connect(database=str(DB), user=str(USER), password=str(PASS), host=str(IP), port=str(PORT))
print("Database Connected: ")

cur = conn.cursor()

# select the values for the index chosen by random
cur.execute("SELECT english,french from verb where id = " + str(randomIndex) + ";")

print("French\t\t\tEnglish")
print("------\t\t\t-------") 

rows = cur.fetchall()
for row in rows:
   print(row[0],'\t\t',row[1].strip())

conn.commit()
conn.close()
