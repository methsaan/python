#! /usr/bin/python3

import psycopg2

conn = psycopg2.connect(database="french_verbs", user="methsaan", password="welcome", host="192.168.2.225", port="5432")
print("Database Connected: ")

cur = conn.cursor()

cur.execute("SELECT english, french from verb;")

print("French English")
print("--------------") 

rows = cur.fetchall()
for row in rows:
   print(row[0],'\t\t',row[1].strip())

conn.commit()
conn.close()
print("Records created successfully");
