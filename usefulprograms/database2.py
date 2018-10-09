#! /usr/bin/python3

import psycopg2

conn = psycopg2.connect(database="french_verbs", user="methsaan", password="welcome", host="192.168.2.225", port="5432")
print("Database Connected: ")

cur = conn.cursor()

cur.execute("DROP TABLE test;")
print("Table dropped: test")
cur.execute("CREATE TABLE test(id serial PRIMARY KEY, sname CHAR(50), roll_num integer);")
print("Table Created: test")

cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (10, 'Sara', 3)");
cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (20, 'Ema', 4)");
cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (30, 'Drabir', 2)");
cur.execute("INSERT INTO test (id, sname, roll_num) \
      VALUES (40, 'Surya', 1)");

cur.execute("SELECT id, sname, roll_num from test")
print("ID   Roll No. Student Name")
print("--------------------------") 
rows = cur.fetchall()
for row in rows:
   print(row[0],' ',str(row[2]).strip(),'      ',row[1].strip())

conn.commit()
conn.close()
print("Records created successfully");
