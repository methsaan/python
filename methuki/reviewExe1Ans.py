#! /usr/bin/python3

# Exercise 1
# Use programmingreminders.txt before asking for help
# 1. ask user for name 4%
# 2. ask user for age 4%
# 3. ask user for favourite decimal number 4%
# 4. create boolean variable of whether the decimal number is equal to 28.5 10%
# 5. if the boolean variable is true print 'That's my favourite number too' using single quotes 9%
# 6. if not print: (name) is (age) years old and his favourite number is (decimal number) using only one command 8%
# 7. create a list of foods 6%
# 8. print the list with the brackets and commas 6%
# 9. print the list without brackets and commas, just side by side with spaces, use the range function 11%
# 10. repeat step 9 but without the range function 11%
# 11. repeat step 10 but each on a new line 7%
# 12. print out the following text 3%
#
#       ---"---\---/---'---\---"
#       |    \   "   \   \   " |
#       |_"_""_"_"_""_""_"_"_"_|
# 13. create a list of 20 integers 2%
# 14. print out the 13th element divided by the 3rd element 4%
# 15. print out the first 5 elements 2%
# 16. print out the last five elements 2%
# 17. print the fifth to the fifteenth counting by 4 2%
# 18. add 3 lines of random text 0%
# 19. delete the text in 1 command using a vi shortcut 2%
# 20. rename this file as reviewExercise1.py 2%
# 21. create a copy of this program called reviewExe1Ans.py 1%
name = input("What is your name? ")
age = int(input("How old are you? "))
favNum = float(input("What is your favourite number? "))
likes28point5 = favNum == 28.5
if likes28point5:
    print('That\'s my favourite number too')
else:
    print(name, "is", age, "years old and his favourite number is", favNum)
foods = ["Biryani", "apple", "rice", "bread", "broccoli"]
print(foods)
for x in range(len(foods)):
    print(foods[x], end=" ", flush=True)
print()
for x in foods:
    print(x, end=" ", flush=True)
print()
for x in foods:
    print(x)
numList = [54, 65, 23, 64, 345756, 423, 75, 6435, 65, 432, 75, 345, 8, 25, -57, 4, 75, 45, 1, -5]
print(numList[12] / numList[2])
print(numList[4:15:4])
