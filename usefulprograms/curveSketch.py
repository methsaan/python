#! /usr/bin/python3

import re
#from tkinter import *
#tk = Tk()
#canvas = Canvas(tk, width=1000, height=1000)
#canvas.pack()

allowedFuncRegex = "x|\*|\*\*|math\.sin|math\.cos|\d|math.log|\+| |\-|\/"

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
        if re.search("-*math\.sin\(({allowedFuncRegex})\)", exp) != None:
            # math.sin(x^2 + math.log(x))
            return exp.replace("math.sin", "math.cos")
        elif re.search("-*math\.cos\(({allowedFuncRegex})\)", exp) != None:
            # math.cos(x^2 - 4x + 1)
            return exp.replace("math.cos", "-math.sin")
        elif exp.isdigit():
            # 46
            return "0"
        elif re.search("\d+\*\(({allowedFuncRegex})\)\^\d+", exp) != None:
            # 22*(x^2 + math.sin(x))^5
            return str(int(re.findall("(?<=\^)\d+", exp)[0]) * int(re.findall("(?=\*)\d+", exp)[0])) + \
                   re.findall("\(({allowedFuncRegex})\)") + str(int(re.findall("(?<=\^)\d+", exp)[0]) - 1)

func = Function("x**2 + 2*x + 1")
print(func.f(5))
print(func.yInt())

#canvas.mainloop()
