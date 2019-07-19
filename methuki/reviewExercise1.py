#! /usr/bin/python3

# Exercise 1
# Use programmingreminders.txt before asking for help
# 1. ask user for name 4 / 4%
# 2. ask user for age 4 / 4%
# 3. ask user for favourite decimal number 1 / 4%
# 4. create boolean variable of whether the decimal number is equal to 28.5 0 / 10%
# 5. if the boolean variable is true print 'That's my favourite number too' using single quotes 5 / 9%
# 6. if not print: (name) is (age) years old and his favourite number is (decimal number) using only one command 2 / 8%
# 7. create a list of foods 6 / 6%
# 8. print the list with the brackets and commas 6 / 6%
# 9. print the list without brackets and commas, just side by side with spaces, use the range function 4 / 11%
# 10. repeat step 9 but without the range function 11 / 11%
# 11. repeat step 10 but each on a new line 0 / 7%
# 12. print out the following text 0.5 / 3%
#
#       ---"---\---/---'---\---"
#       |    \   "   \   \   " |
#       |_"_""_"_"_""_""_"_"_"_|
# 13. create a list of 20 integers 2 / 2%
# 14. print out the 13th element divided by the 3rd element 0.5 / 4%
# 15. print out the first 5 elements 1 / 2%
# 16. print out the last five elements 0 / 2%
# 17. print the fifth to the fifteenth counting by 4 2 / 2%
# 18. add 3 lines of random text -5 / 0%
# 19. delete the text in 1 command using a vi shortcut 2 / 2%
# 20. rename this file as reviewExercise1.py 0 / 2%
# 21. create a copy of this program called reviewExe1Ans.py 1 / 1%
name = input("What Is Your Name? ")
age = float(input("How Old Are You? "))
ask1 = input("What Is Your Favourite Decimal Number? ")
if ask1 == 28.5:
    print('that\'s my favourite number too!!')
else:
    print(name, "is", age, "years old and his favourite decimal number is", ask1)
food = ["Apples", "Carrot", "Bread", "Bananas", "Rice"]
print(food)
for m in range(len(food)):
    print(food[m])
for m in food:
    print(m ,end=" ", flush=True)
print()
print("---\"---\\---/---'---\\---\"\n|\t\\\t\"\t\\\t\\\t\" |\n|_\"_\"\"_\"_\"_\"\"_\"\"_\"_\"_\"_|")
ints = [34,35,36,37,38,39,45,46,47,48,49,3,4,5,6,7,89,0,56,45]
print(ints[12]/ints[2])
print(ints[:5])
print(ints[-5:])
print(ints[4:15:4])
