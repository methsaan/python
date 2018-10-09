#! /usr/bin/python3

import psycopg2
conn = psycopg2.connect(database="french_verbs", user="methsaan", password="welcome", host="192.168.2.225", port="5432")
print("Database Connected....")
