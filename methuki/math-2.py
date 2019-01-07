#! /usr/bin/python3

print("*** Calculator ***")
print()

# declare a variable called 'operator' to store user input
# is 'operator' a string ? no
# 'operator' is a variable, which stores a string input
operator = input("What operator do you want to do today (+,-,*,/,%,**) ? ")
operand1 = float(input("Enter first number: "))
operand2 = float(input("Enter second number: ")) 

print("Your operator was: " + operator) 
if operator == "+":
	print(operand1+operand2)
elif operator == "-":
	print(operand1-operand2)
elif operator == "*":
	print(operand1*operand2)
elif operator == "/":
	print(operand1/operand2)
elif operator == "%":
	print(operand1%operand2)
elif operator == "**":
	print(operand1**operand2)
