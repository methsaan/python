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
      VVVVV               VVVVvvV                  VVvvVV            ''', 'yellow');cprint('''       |v|                 |v||                     ||||              
       |||                 ||v|                     |v||              
       | |                 ||||                     |}||              
       |||                 |{}|                     ||||             
       |||                 ||v|                     |v||              ''', 'red');cprint('''
      VVVVV               VvvVVVV                 VvvVVVV             
^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^ ^ ^^^^ ^^^ ^^^^
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^  ^^^^^^^^^^^  ^^^^ ^^
^^ ^^^^^^^^^^^^^^^^^^^ ^^^^ ^ ^ ^^ ^^^^^^^^^ ^^^^^^^^^^^^^^^^^  ^^^^ ^
^^^^^^^^^^ ^^^ ^^^^^^^ ^^^^^^^^^^ ^^^^ ^^^^^^^^^ ^^^^^^^^  ^^^^  ^^^^ 
^^^^ ^^ ^^^^^^ ^^^^^^^^^^^^ ^^ ^ ^^^^^ ^^^^^^^^^^^^^ ^^^ ^^ ^^  ^^^ ^^ 
^^ ^^^^^^^^^^^^^^^^^^^ ^^^^ ^ ^ ^^ ^^^^^^^^^ ^^^^^^^^^^^^^^^^^  ^^^^ ^
1                                                                    70
	''','yellow')
	rand_x = random.choice([random.randrange(1, 69)])
	for y in range(2, 20):
		if y == 7 or y == 14:
			guess_x = int(input("Guess where the apple is going to fall (1-69) ?"))
			if guess_x == rand_x:
				subprocess.call("clear", shell=True)
				print("You are correct")
				got_correct = True
				break
		print_char(rand_x, y, "0", "green")
		time.sleep(0.5)
		#print(rand_x)
		print_char(rand_x+1, y, "\b ", "green")
	print("Correct location:", rand_x)
	time.sleep(3)
	if got_correct:
		continue
