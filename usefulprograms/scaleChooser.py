#! /usr/bin/python3

import subprocess as sp
import random
import time

notes = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
notes2 = ["C", "C#", "D", "D#", "E", "F", "Gb", "G", "G#", "A", "Bb", "B"]
types = [" Minor Chord Broken", " Dominant 7th Chord Broken", " Dominant 7th Chord Solid", " Diminished 7th Chord Broken", " Diminished 7th Chord Solid", " Minor Arpeggio"]
types2 = [" Harmonic minor scale", " Melodic minor scale"]

while True:
    sp.call("clear", shell=True)
    scale = random.choice([random.choice(notes) + random.choice([" Major Scale", " Major Chord Broken", " Major Arpeggio"]), random.choice(notes2) + (random.choice(types+types2))])
    print(scale)
    time.sleep(35)
