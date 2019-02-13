#! /usr/bin/python3

word = input("Enter a word: ")
doubleLetter = int(input("Enter the number of double letter scores: "))
tripleLetter = int(input("Enter the number of triple letter scores: "))
doubleWord = bool(int(input("Enter the number of double word scores: ")))
tripleWord = bool(int(input("Enter the number of triple word scores: ")))
letterscores = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"x":8,"y":4,"z":10}
score = 0
for x in range(len(word)):
    score += letterscores[word[x:x+1]]
score -= doubleLetter
score += doubleLetter*2
score -= tripleLetter
score += tripleLetter*3
score *= 2 if doubleWord == True else 1
score *= 3 if tripleWord == True else 1
print("The scrabble score for your word is", score)
