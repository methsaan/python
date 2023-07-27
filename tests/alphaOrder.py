#! /usr/bin/python3

from operator import itemgetter

users = [
    {'fname' : 'waa', 'lname' : 'wiw'},
    {'fname' : 'woo', 'lname' : 'asd'},
    {'fname' : 'waa', 'lname' : 'why'},
    {'fname' : 'but', 'lname' : 'ho'},
    {'fname' : 'puip', 'lname' : 'ha'}
]

for x in sorted(users, key=itemgetter("fname", "lname")):
    print(x)
