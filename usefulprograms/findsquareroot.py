#! /usr/bin/python3

import math

square = int(input("Enter a 3-digit number: "))
digits = str(square)
sqrtOnes = {0: [0], 1 : [1, 9], 2 : [], 3: [], 4: [2, 8], 5: [5], 6: [4, 6], 7: [], 8: [], 9: [3, 7]}
print(" ", square)
sqrtTenth = int(math.sqrt(int(digits[0])))
print("  |")
print("   \\")
print("    \\")
print("     \\")
print("      |")
print("      V")
print("", str(sqrtTenth) + "\u00B2 <", digits[0], "<", str(sqrtTenth+1) + "\u00B2") 
print("===\n")
sqrtOnesOptions = sqrtOnes[int(digits[2])]
ans = None
print("Options: ", end="", flush=True)
for x in sqrtOnesOptions:
    print(str(sqrtTenth)+str(x), end=" ", flush=True)
print()
for x in sqrtOnesOptions:
    sqrtOption = int(str(sqrtTenth)+str(x))
    print(sqrtOption, "^ 2 =", sqrtOption**2)
    if sqrtOption**2 == square:
        ans = sqrtOption
if ans == None:
    print("Not a perfect square")
else:
    print("Answer:", ans)
# prove theory of finding squareroot for 3 digit number in range
# above
