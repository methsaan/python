#! /usr/bin/python3

import subprocess
import time
import random
import sys
from termcolor import colored, cprint

def print_char(x, y, char, color):
    cprint("\033["+str(y)+";"+str(x)+"H"+char, color)

rand_x = 1
got_correct = False
while True:
	subprocess.call("clear", shell=True)
	cprint('''
(U U U O U UU U Oo)  (UUU Ooo U UU UUU U)  (ouuuuO uUUU UUU O OUU UU)
 (oUUUO UU UU UUU)    (U UUUUUU O uuUO)     (uUUU uuuUUo OO UUuuu U) 
  (UUuO UU UUUUU)      (uuUUUU UUU uU)       ( UOoU UuuOoUU O O Ou)  
   (UU uO Oo uU)        (UuO uU O UU)         (uUU O UUU O uUUUou)
      VVVVV               VVVVvvV                  VVvvVV            ''', 'green');cprint('''       |v|                 |v||                     ||||              
       |||                 ||v|                     |v||              
       | |                 ||||                     |}||              
       |||                 |{}|                     ||||             
       |||                 ||v|                     |v||              
      ^^^^^               ^^^^^^^                 ^^^^^^^''', 'yellow');cprint('''^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^ ^ ^^^^ ^^^ ^^^^
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^  ^^^^^^^^^^^  ^^^^ ^^
^^ ^^^^^^^^^^^^^^^^^^^ ^^^^ ^ ^ ^^ ^^^^^^^^^ ^^^^^^^^^^^^^^^^^  ^^^^ ^
^^^^^^^^^^ ^^^ ^^^^^^^ ^^^^^^^^^^ ^^^^ ^^^^^^^^^ ^^^^^^^^  ^^^^  ^^^^ 
^^^^ ^^ ^^^^^^ ^^^^^^^^^^^^ ^^ ^ ^^^^^ ^^^^^^^^^^^^^ ^^^ ^^ ^^  ^^^ ^^ 
^^ ^^^^^^^^^^^^^^^^^^^ ^^^^ ^ ^ ^^ ^^^^^^^^^ ^^^^^^^^^^^^^^^^^  ^^^^ ^''', 'green')
	cprint('''1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^70''', 'yellow')
	rand_x = random.choice([random.randrange(1, 69)])
	for y in range(2, 20):
		if y == 7 or y == 14:
			print_char(1, 17+int(y/7)+(int(y/7)+1), "Guess where the apple is going to fall (1-69) ? ", "white")
			guess_x = int(input())
			if guess_x == rand_x:
				got_correct = True
				break
		print_char(rand_x, y, "{}", "red")
		time.sleep(0.3)
		#print(rand_x)
		print_char(rand_x+1, y, " \b\b  ", "red")
	print_char(1, 25, "Correct location: " + str(rand_x), "white")
	print(guess_x, rand_x)
	if got_correct:
		print_char(1, 24, "You are correct", "white")
		print_char(rand_x, 19, "<>", "red")
		time.sleep(3)
		continue
	else:
		print_char(rand_x, 19, "~~", "red")
		time.sleep(3)
		continue
