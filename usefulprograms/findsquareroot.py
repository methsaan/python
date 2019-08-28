#! /usr/bin/python3

import math

start_num = 10
end_num = 32

square = int(input("Enter a 3-digit number: "))
digits = str(square)
sqrtOnes = {1 : [1, 9], 2 : [], 3: [], 4: [2, 8], 5: [5], 6: [4, 6], 7: [], 8: [], 9: [3, 7]}
print(square)
sqrtTenth = int(math.sqrt(int(digits[0])))
print("|")
print("V")
print(str(sqrtTenth) + "\u00B2 <", digits[0], "<", str(sqrtTenth+1) + "\u00B2") 
print(sqrtOnes[int(digits[2])])
for x in 
# prove theory of finding squareroot for 3 digit number in range
# above
