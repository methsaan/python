#! /usr/bin/python3

import re
#from tkinter import *
#tk = Tk()
#canvas = Canvas(tk, width=1000, height=1000)
#canvas.pack()

"""
(?<=\*\*)(?<=(.*\).*){0})(?<=(.*\(.*){0})\d+|(?<=\*\*)(?<=(.*\).*){1})(?<=(.*\(.*){1})\d+|(?<=\*\*)(?<=(.*\).*){2})(?<=(.*\(.*){2})\d+|(?<=\*\*)(?<=(.*\).*){3})(?<=(.*\(.*){3})\d+|(?<=\*\*)(?<=(.*\).*){4})(?<=(.*\(.*){4})\d+|(?<=\*\*)(?<=(.*\).*){5})(?<=(.*\(.*){5})\d+|(?<=\*\*)(?<=(.*\).*){6})(?<=(.*\(.*){6})\d+|(?<=\*\*)(?<=(.*\).*){7})(?<=(.*\(.*){7})\d+|(?<=\*\*)(?<=(.*\).*){8})(?<=(.*\(.*){8})\d+
"""

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
        print("Original:", exp)
        if re.search(r"\d+\*\(" + allowedFuncRegex + r"\)\*\*\d+", exp) != None:
            # power function of a function
            # 22*(x**2 + math.sin(x))**5
            print("power function of a triangle")
            powerRegex = ""
            for bracketCnt in range(8):
                powerRegexTemp = r"(?<=\*\*)"
                powerRegexTemp += r"(?<=(.*\).*){" + str(bracketCnt) + r"})"
                powerRegexTemp += r"(?<=(.*\(.*){" + str(bracketCnt) + r"})"
                powerRegexTemp += "\d+"
                powerRegex += powerRegexTemp + "|"
            powerRegexTemp = r"(?<=\*\*)"
            powerRegexTemp += r"(?<=(.*\).*){8})"
            powerRegexTemp += r"(?<=(.*\(.*){8})"
            powerRegexTemp += "\d+"
            powerRegex += powerRegexTemp
            
            print(powerRegex)
            print("power:", re.findall(powerRegex, exp))
            print("constant:", re.findall(r"(?=\*)\d+", exp))
            print("function:", re.findall(r"\(" + allowedFuncRegex + r"\)", exp))
            return str(int(re.findall(r"(?<=\*\*)\d+", exp)[0]) * int(re.findall(r"(?=\*)\d+", exp)[0])) + \
                   re.findall(r"\(" + allowedFuncRegex + r"\)")[0] + str(int(re.findall(r"(?<=\*\*)\d+", exp)[0]) - 1)
        elif re.search(r"-*math\.sin\(" + allowedFuncRegex + r"\)", exp) != None:
            # sin of a function
            # math.sin(x**2 + math.log(x))
            print("sin of a triangle")
            return exp.replace("math.sin", "math.cos")
        elif re.search(r"-*math\.cos\(" + allowedFuncRegex + r"\)", exp) != None:
            # cos of a function
            # math.cos(x**2 - 4*x + 1)
            print("cos of a triangle")
            return exp.replace("math.cos", "-math.sin")
        elif exp.isdigit():
            # constant
            # 46
            print("constant")
            return "0"

func = Function("x**2 + 2*x + 1")
print(func.f(5))
print(func.yInt())

string1 = "math.sin(x**2 + math.log(x))"
string2 = "math.cos(x**2 - 4*x + 1)"
string3 = "46"
string4 = "22*((x+2)**2 + math.sin(x))**5"

print(func.differentiateBasic(string1))
print(func.differentiateBasic(string2))
print(func.differentiateBasic(string3))
print(func.differentiateBasic(string4))

#canvas.mainloop()
