#! /usr/bin/python3

import subprocess as sp

print ('This program helps you play Rock Paper Scissors! You will need 2 people to play.')

player1 = input('Player 1 what is your name? ')

player2 = input('Player 2 what is your name? ')

choose1 = input(player2 + " turn around and let " + player1 + " choose rock, paper, or scissors.") 
sp.call("clear \n", shell=True)
choose2 = input(player2 + " choose rock, paper, or scissors. ")

print (player1 + " chose " + choose1)
print (player2 + " chose " + choose2)

