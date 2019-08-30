#! /usr/bin/python3

import random
import time
import sys
import subprocess as sp

class song:
    def __init__(self, name, genre, prefForce, key, form, tempo, structure, artist):
        self.name = name
        self.genre = genre
        self.prefForce = prefForce
        self.key = key
        self.form = form
        self.tempo = tempo
        self.structure = structure
        self.artist = artist
song1 = song("A Midsummer Night's Dream", "concert overture", "symphony orchestra", "E major", "sonata form", "unknown", "unknown", "Felix Mendelssohn")
song2 = song("Revolutionary Etude", "solo piano work", "piano", "C minor", "ABA", "allegro con fuoco", "unknown", "Frederic Chopin")
song3 = song("Petrushka", "ballet", "large orchestra with expanded percussion (including piano)", "unknown", "rondo form (ABACABA)", "unknown", "unknown", "Igor Stravinsky")
song4 = song("Dripsody", "electronic music", "recorded sound of dripping water", "unknown", "unknown", "1'28\"", "unknown", "Hugh LeCaine")
song5 = song("Ko-Ko", "twelve-bar blues", "trumpet, trombone, clarinet, saxophone, drums, double bass, guitar, piano", "E flat minor", "unknown", "unknown", "introduction, seven choruses, coda", "Duke Ellington")
score = 0
for x in range(int(sys.argv[1])):
    sp.call("clear", shell=True)
    songList = [song1, song2, song3, song4, song5]
    datalist = ["Genre", "Preforming forces", "Key", "Form", "Tempo", "Structure", "Artist"]
    propertyList = ["genre", "prefForce", "key", "form", "tempo", "structure", "artist"]
    randSong = random.choice(songList)
    randData = random.choice(datalist)
    randProperty = propertyList[datalist.index(randData)]
    guess = input(str(x+1) + ". " + randData + " of " + randSong.name + ": ")
    if guess == eval("randSong." + randProperty):
        print("Correct")
        time.sleep(1)
        score += 1
    else:
        print("Answer:", eval("randSong." + randProperty))
        time.sleep(1)
print(str(score/int(sys.argv[1])*100) + "%")
