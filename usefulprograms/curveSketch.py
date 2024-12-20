#! /usr/bin/python3

import re
#from tkinter import *
#tk = Tk()
#canvas = Canvas(tk, width=1000, height=1000)
#canvas.pack()

allowedFuncRegex = r"[x|\*{1,2}|math\.sin\(.+?\)|math\.cos\(.+?\)|\d|math.log\(.+?\)|\+| |\-|\/]+"

class Function:
    def __init__(self, funcExp):
        self.funcExp = funcExp
    def f(self, x):
        return int(eval(self.funcExp))
    def yInt(self):
        x = 0
        return int(eval(self.funcExp))
    def differentiateBasic(self, exp):
        """
        Differentiate simple term or apply chain rule only to the most outer
        function of a composite function term
        """
        if re.search(r"-?\d+\*\(" + allowedFuncRegex + r"\)\*\*-?\d+", exp) != None:
            # power function of a function
            # 22*(x**2 + math.sin(x))**5
            power = int(re.findall(r"-?\d+$", exp)[0])
            constant = int(re.findall(r"^-?\d+", exp)[0])
            function = re.findall(r"\(" + allowedFuncRegex + r"\)", exp)[0]
            return str(power * constant) + "*" + function + "**" + str(power - 1)
        elif re.search(r"-?math\.sin\(" + allowedFuncRegex + r"\)", exp) != None:
            # sin of a function
            # math.sin(x**2 + math.log(x))
            return exp.replace("math.sin", "math.cos")
        elif re.search(r"-?math\.cos\(" + allowedFuncRegex + r"\)", exp) != None:
            # cos of a function
            # math.cos(x**2 - 4*x + 1)
            return exp.replace("math.cos", "-math.sin")
        elif re.search(r"-?math\.log\(" + allowedFuncRegex + r" *, *\d+\)", exp) != None:
            # log of a function
            # math.log(x**2 + 2*x - 4, 3)
            function = exp[exp.index("(") + 1:exp.index(",")]
            base = exp[exp.index(",") + 1:exp.index(")")]
            return " 1 / ((" + function + ") * math.log(" + base.strip() + ", math.e))"
        elif exp.isdigit():
            # constant
            # 46
            return "0"

func = Function("x**2 + 2*x + 1")
print("f(x) = x**2 + 2*x + 1")
print("f(5):", func.f(5))
print("y-int:", func.yInt())

string1 = "-22*((x+2)**2 + math.sin(x))**5"
string2 = "22*(x)**-5"
string3 = "-1*(x)**5"
string4 = "47*(x)**1"
string5 = "math.sin(x**2 + math.log(x))"
string6 = "math.cos(x**2 - 4*x + 1)"
string7 = "math.sin(x)"
string8 = "math.cos(x)"
string9 = "46"
string10 = "math.log(x**2 + 2*x - 4, 3)"
string11 = "math.log(x, 4)"

print(func.differentiateBasic(string1))
print(func.differentiateBasic(string2))
print(func.differentiateBasic(string3))
print(func.differentiateBasic(string4))
print(func.differentiateBasic(string5))
print(func.differentiateBasic(string6))
print(func.differentiateBasic(string7))
print(func.differentiateBasic(string8))
print(func.differentiateBasic(string9))
print(func.differentiateBasic(string10))
print(func.differentiateBasic(string11))

#canvas.mainloop()
