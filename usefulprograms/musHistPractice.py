#! /usr/bin/python3

import random
import time

class song:
    def __init__(self, name, genre, prefForce, key, form, tempo, structure):
        self.name = name
        self.genre = genre
        self.prefForce = prefForce
        self.key = key
        self.form = form
        self.tempo = tempo
        self.structure = structure
song1 = song("A Midsummer Night's Dream", "concert overture", "symphony orchestra", "E major", "sonata form", "unknown", "unknown")
song2 = song("Revolutionary Etude", "solo piano work", "piano", "C minor", "ABA", "allegro con fuoco", "unknown")
song3 = song("Petrushka", "ballet", "large orchestra with expanded percussion (including piano)", "unknown", "rondo form (ABACABA)", "unknown", "unknown")
song4 = song("Dripsody", "electronic music", "recorded sound of dripping water", "unknown", "unknown", 
