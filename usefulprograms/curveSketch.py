#! /usr/bin/python3

import re
import math
#from tkinter import *
#tk = Tk()
#canvas = Canvas(tk, width=1000, height=1000)
#canvas.pack()

allowedFuncRegex = r"[x|\*{1,2}|math\.sin\(.+?\)|math\.cos\(.+?\)|\d|math.log\(.+?\)|math.e|\+| |\-|\/]+"

class Function:
    def __init__(self, funcExpr, start, end):
        self.funcExpr = funcExpr
        self.start = start
        self.end = end
    def f(self, x):
        """
        Evaluate self.funcExp at x
        """
        return float(eval(self.funcExpr))
    def getyInt(self):
        """
        Return y-intercept of self.funcExp
        """
        x = 0
        return float(eval(self.funcExpr))
    def correctBrackets(self, string):
        endBracketIndices = [m.start(0) for m in re.finditer(r"\)", string)] 
        for i in range(len(endBracketIndices)):
            if string[:endBracketIndices[i]].count("(") < i + 1:
                return False
        return string.count("(") == string.count(")")
    def differentiateOuter(self, expr):
        """
        Apply chain rule, product rule, or quotient rule to a basic function
        or to the most outer function of a composite function term, set up
        inner function derivative step for chain rule, product rule or
        quotient rule.
        """
        if re.search(r"^\(*x\)*$", expr) != None and expr.count("(") == expr.count(")"):
            return "1"
        elif re.search(r"^\(*-x\)*$", expr) != None and expr.count("(") == expr.count(")"):
            return "-1"
        elif re.search(r"^-?[\d|\.]+ \* \(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\) \*\* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \* x \*\* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \* \(x" + allowedFuncRegex + r"\) \*\* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \* \(" + allowedFuncRegex + r"x\) \*\* -?[\d|\.]+$", expr) != None:
            # power function of a function (with constant multiple)
            # 22 * (x ** 2 + math.sin(x)) ** 5
            power = float(re.findall(r"-?[\d|\.]+$", expr)[0])
            constant = float(re.findall(r"^-?[\d|\.]+", expr)[0])
            function = re.findall(r"\* " + allowedFuncRegex + r" \*\*", expr)[0][2:-3]
            return ("" if function == "x" else "(") + \
                   str(power * constant) + " * " + function + " ** " + str(power - 1) +\
                   ("" if function == "x" else (") * (DERIVATIVE" + function + ")"))
        elif re.search(r"^-?[\d|\.]+ \* \(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \* -?x$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \* -?\(x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \* -?\(" + allowedFuncRegex + r"x\)$", expr) != None:
            # constant multiple of a function (const first)
            # 47 * (x ** 2 + math.log(x, 4))
            constant = re.findall(r"^-?[\d|\.]+", expr)[0]
            function = re.findall(r"\* " + allowedFuncRegex, expr)[0][2:]
            return ("" if function == "x" else "(") + constant + ("" if function == "x" else (") * (DERIVATIVE(" + function + "))"))
        elif re.search(r"^-?\(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\) \* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?x \* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?\(x" + allowedFuncRegex + r"\) \* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?\(" + allowedFuncRegex + r"x\) \* -?[\d|\.]+$", expr) != None:
            # constant multiple of a function (function first)
            # (x ** 2 + math.log(x, 4)) * 35
            constant = re.findall(r"-?[\d|\.]+$", expr)[0]
            function = re.findall(allowedFuncRegex + r" \*", expr)[0][:-2]
            return ("" if function == "x" else "(") + constant + ("" if function == "x" else (") * (DERIVATIVE(" + function + "))"))
        elif re.search(r"^\(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\) \*\* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?x \*\* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?\(x" + allowedFuncRegex + r"\) \*\* -?[\d|\.]+$", expr) != None or\
                 re.search(r"^-?\(" + allowedFuncRegex + r"x\) \*\* -?[\d|\.]+$", expr) != None:
            # power function of a function (without constant multiple)
            # (x ** 2 + math.sin(x)) ** 4
            power = re.findall(r"-?[\d|\.]+$", expr)[0]
            function = re.findall(allowedFuncRegex + r" \*\*", expr)[0][:-3]
            return ("" if function == "x" else "(") + \
                   power  + " * " + function + " ** " + str(int(power) - 1) +\
                   ("" if function == "x" else (") * (DERIVATIVE(" + function + "))"))
        elif re.search(r"^-?[\d|\.]+ \*\* \(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \*\* x$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \*\* \(x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?[\d|\.]+ \*\* \(" + allowedFuncRegex + r"x\)$", expr) != None:
            # exponential function
            # 6 ** (x ** 2 + math.sin(2 * x) - 3)
            base = re.findall("^-?[\d|\.]+", expr)[0]
            function = "x" if "(" not in expr else expr[expr.index("(") + 1:expr.index(")") + 1]
            return ("(" if function == "x" else "((") + \
                   base + " ** (" + function + ")) * (math.log(" + base.strip() + ", math.e))" + \
                   ("" if function == "x" else ") * (DERIVATIVE(" + function + "))")
        elif re.search(r"^-?math\.sin\(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?math\.sin\(x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?math\.sin\(" + allowedFuncRegex + r"x\)$", expr) != None or\
                 re.search(r"^-?math\.sin\(x\)$", expr) != None:
            # sin of a function
            # math.sin(x ** 2 + math.log(x))
            derivative = expr.replace("math.sin", "math.cos")
            function = expr[expr.index("(") + 1:-1]
            derivative = ("(" if function != "x" else "") + derivative
            if function != "x":
                derivative += ") * (DERIVATIVE(" + function + "))"
            return derivative
        elif re.search(r"^-?math\.cos\(" + allowedFuncRegex + r"x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?math\.cos\(x" + allowedFuncRegex + r"\)$", expr) != None or\
                 re.search(r"^-?math\.cos\(" + allowedFuncRegex + r"x\)$", expr) != None or\
                 re.search(r"^-?math\.cos\(x\)$", expr) != None:
            # cos of a function
            # math.cos(x ** 2 - 4 * x + 1)
            derivative = expr.replace("math.cos", "-math.sin")
            function = expr[expr.index("(") + 1:-1]
            derivative = ("(" if function != "x" else "") + derivative
            if function != "x":
                derivative += ") * (DERIVATIVE(" + function + "))"
            return derivative
        elif re.search(r"^-?math\.log\(" + allowedFuncRegex + r"x" + allowedFuncRegex + r" *, *[\d|\.]+\)$", expr) != None or\
                 re.search(r"^-?math\.log\(x *, *[\d|\.]+\)$", expr) != None or\
                 re.search(r"^-?math\.log\(x" + allowedFuncRegex + r" *, *[\d|\.]+\)$", expr) != None or\
                 re.search(r"^-?math\.log\(" + allowedFuncRegex + r"x *, *[\d|\.]+\)$", expr) != None:
            # log of a function
            # math.log(x ** 2 + 2 * x - 4, 3)
            function = expr[expr.index("(") + 1:expr.index(",")]
            base = expr[expr.index(",") + 1:-1]
            return ("" if function == "x" else "(") + \
                    ("(-" if expr.startswith("-") else "(") + "1) / ((math.log(" + base.strip() + ", math.e)) * (" + function + "))" + \
                    ("" if function == "x" else (") * (DERIVATIVE(" + function + "))"))
        elif re.search(allowedFuncRegex, expr) != None and "x" not in expr:
            # constant
            # 46
            return "0"
        else:
            # Product rule and quotient rule, error if neither
            # (x ** 2 + 3 * x - 7) * (math.sin(x) + 6)
            # (x - x ** 3) / (math.log(x, 7) - x)
            productRuleIdx = -1
            quotientRuleIdx = -1
            for idx in [m.start() for m in re.finditer(r"\*", expr)]:
                if expr[:idx - 1].count("(") == expr[:idx - 1].count(")") and expr[idx + 2:].count("(") == expr[idx + 2:].count(")"):
                    productRuleIdx = idx
            for idx in [m.start() for m in re.finditer(r"/", expr)]:
                if expr[:idx - 1].count("(") == expr[:idx - 1].count(")") and expr[idx + 2:].count("(") == expr[idx + 2:].count(")"):
                    quotientRuleIdx = idx
            if quotientRuleIdx == -1:
                left = expr[:productRuleIdx - 1]
                right = expr[productRuleIdx + 2:]
                return left + " * (DERIVATIVE(" + right + ")) + " + right + " * (DERIVATIVE(" + left + "))"
            elif productRuleIdx == -1:
                left = expr[:quotientRuleIdx - 1]
                right = expr[quotientRuleIdx + 2:]
                return "(" + right + " * (DERIVATIVE(" + left + ")) - " + left + " * (DERIVATIVE(" + right + "))) / (" + \
                        right + " ** 2)"
            else:
                return "ERROR"
    def getFirstDerivative(self, number=0):
        expr = self.funcExpr
        exprSplit = [i.strip() for i in re.split(r"([\+-])", expr)]
        exprTerms = [exprSplit[0]] + [(("-1 * " + (exprSplit[i + 1])) if (exprSplit[i] == "-") else (exprSplit[i + 1])) \
                                       for i in range(1, len(exprSplit) - 1, 2)]
        i = 0
        while i < len(exprTerms) - 1:
            tempStr = exprTerms[i]
            j = i + 1
            while tempStr.count("(") > tempStr.count(")"):
                tempStr += " + " + exprTerms[j]
                j += 1
            del exprTerms[i:j]
            exprTerms.insert(i, tempStr)
            i += 1
        for n in range(len(exprTerms)):
            if exprTerms[n].startswith("+"):
                exprTerms[n] = exprTerms[n][1:]
        exprTerms = [n for n in exprTerms if n != ""]
        exprTermsDerivative = [self.differentiateOuter(i) for i in exprTerms]
        derivativeStr = " + ".join(exprTermsDerivative)
        derivativeStr = derivativeStr.replace("+ +", "+ ")
        if number == 1:
            print("ZERO", derivativeStr)
            print()
        derivativeStr = re.sub("\s\+\s+\+\s", " + ", derivativeStr)
        if number == 1:
            print("ONE", derivativeStr)
            print()
        derivativeStr = re.sub("\*\s+1\s+\*\s+1\s+\*", "*", derivativeStr)
        if number == 1:
            print("TWO", derivativeStr)
            print()
        derivativeStr = re.sub("\s\*\*\s1\.0", "", derivativeStr)
        if number == 1:
            print("THREE", derivativeStr)
            print()
        derivativeStr = re.sub("\s\*\*\s1", "", derivativeStr)
        if number == 1:
            print("FOUR", derivativeStr)
            print()
        #if "DERIVATIVE" not in derivativeStr:
        #    derivativeStr = re.sub(r"(\(\()(\d+)(\)\))", r"\2", derivativeStr)
        if number == 1:
            print("FIVE", derivativeStr)
            print()
        # ISSUE
        #if "DERIVATIVE" not in derivativeStr:
        #    derivativeStr = re.sub(r"(\()(\d+)(\))", r"\2", derivativeStr)
        if number == 1:
            print("SIX", derivativeStr)
            print()
        derivativeStr = re.sub(r"(1)(\s\*\s)(\-?[\d|\.]+)", r"\3", derivativeStr)
        if number == 1:
            print("SEVEN", derivativeStr)
            print()
        derivativeStr = re.sub(r"(\-?[\d|\.]+)(\s\*\s)(1)", r"\1", derivativeStr)
        if number == 1:
            print("EIGHT", derivativeStr)
            print()
        derivativeStr = re.sub(r"(\-1)(\s\*\s)(\-?[\d|\.]+)", r"-\3", derivativeStr)
        if number == 1:
            print("NINE", derivativeStr)
            print()
        derivativeStr = re.sub(r"(\-?[\d|\.]+)(\s\*\s)(\-1)", r"-\1", derivativeStr)
        if number == 1:
            print("TEN", derivativeStr)
            print()
        bracketPairs = [(m.start(), m.end()) for m in re.finditer(r"^[\(\d+][\d|\.|\s|\+|\*|\-|\/]+[\d+\)]$", derivativeStr)]
        for bracketPair in bracketPairs:
            if self.correctBrackets(derivativeStr[bracketPair[0]:bracketPair[1]]) and \
               "x" not in derivativeStr[bracketPair[0]:bracketPair[1]]:
                derivativeStr = derivativeStr.replace(derivativeStr[bracketPair[0]:bracketPair[1]], "(" + str(eval(derivativeStr[bracketPair[0]:bracketPair[1]])) + ")")
        if "DERIVATIVE" not in derivativeStr:
            return derivativeStr
        else:
            derivativeTempList = re.findall(r"DERIVATIVE\(" + allowedFuncRegex, derivativeStr)
            for d in range(len(derivativeTempList)):
                temp = "DERIVATIVE("
                while temp.count("(") != temp.count(")"):
                    temp += derivativeTempList[d][len(temp):len(temp) + 1]
                    if len(temp) == len(derivativeTempList[d]):
                        return "ERROR"
                derivativeTempList[d] = temp
            for func in derivativeTempList:
                funcPortion = func[11:-1]
                while len(funcPortion) > 1 and funcPortion[0] == "(" and funcPortion[-1] == ")" and self.correctBrackets(funcPortion[1:-1]):
                    funcPortion = funcPortion[1:-1]
                derivativeStr = derivativeStr.replace(func, Function(funcPortion, self.start, self.end).getFirstDerivative())
            if number == 1:
                print("ZERO", derivativeStr)
                print()
            derivativeStr = re.sub("\s\+\s+\+\s", " + ", derivativeStr)
            if number == 1:
                print("ONE", derivativeStr)
                print()
            derivativeStr = re.sub("\*\s+1\s+\*\s+1\s+\*", "*", derivativeStr)
            if number == 1:
                print("TWO", derivativeStr)
                print()
            derivativeStr = re.sub("\s\*\*\s1\.0", "", derivativeStr)
            if number == 1:
                print("THREE", derivativeStr)
                print()
            derivativeStr = re.sub("\s\*\*\s1", "", derivativeStr)
            if number == 1:
                print("FOUR", derivativeStr)
                print()
            #if "DERIVATIVE" not in derivativeStr:
            #    derivativeStr = re.sub(r"(\(\()(\d+)(\)\))", r"\2", derivativeStr)
            if number == 1:
                print("FIVE", derivativeStr)
                print()
            # ISSUE
            #if "DERIVATIVE" not in derivativeStr:
            #    derivativeStr = re.sub(r"(\()(\d+)(\))", r"\2", derivativeStr)
            if number == 1:
                print("SIX", derivativeStr)
                print()
            derivativeStr = re.sub(r"(1)(\s\*\s)(\-?[\d|\.]+)", r"\3", derivativeStr)
            if number == 1:
                print("SEVEN", derivativeStr)
                print()
            derivativeStr = re.sub(r"(\-?[\d|\.]+)(\s\*\s)(1)", r"\1", derivativeStr)
            if number == 1:
                print("EIGHT", derivativeStr)
                print()
            derivativeStr = re.sub(r"(\-1)(\s\*\s)(\-?[\d|\.]+)", r"-\3", derivativeStr)
            if number == 1:
                print("NINE", derivativeStr)
                print()
            derivativeStr = re.sub(r"(\-?[\d|\.]+)(\s\*\s)(\-1)", r"-\1", derivativeStr)
            if number == 1:
                print("TEN", derivativeStr)
                print()
            bracketPairs = [(m.start(), m.end()) for m in re.finditer(r"^[\(\d+][\d|\.|\s|\+|\*|\-|\/]+[\d+\)]$", derivativeStr)]
            for bracketPair in bracketPairs:
                if self.correctBrackets(derivativeStr[bracketPair[0]:bracketPair[1]]) and \
                   "x" not in derivativeStr[bracketPair[0]:bracketPair[1]]:
                    derivativeStr = derivativeStr.replace(derivativeStr[bracketPair[0]:bracketPair[1]], "(" + str(eval(derivativeStr[bracketPair[0]:bracketPair[1]])) + ")")
            return derivativeStr
    def getSecondDerivative(self, number=0):
        return Function(self.getFirstDerivative(), self.start, self.end).getFirstDerivative(number)
    def getSignChanges(self):
        roots = []
        interval = (self.end - self.start) / 2
        signChangeRanges = []
        for x in range(13):
            interval /= 1.99
            i = self.start
            notCheckedCnt = 0
            while i < self.end:
                checked = False
                for y in signChangeRanges:
                    if i >= y[0] and i + interval <= y[1]:
                        checked = True
                if checked:
                    i += interval
                    continue
                notCheckedCnt += 1
                if (self.f(i) > 0 and self.f(i + interval) < 0) or (self.f(i + interval) > 0 and self.f(i) < 0):
                    signChangeRanges.append((i, i + interval))
                i += interval
            if notCheckedCnt == 0:
                break
        for signChangeRange in signChangeRanges:
            low = signChangeRange[0]
            high = signChangeRange[1]
            while round(low, 6) != round(high, 6):
                mid = (low + high) / 2
                if self.f(mid) < 0:
                    if self.f(signChangeRange[0]) > self.f(signChangeRange[1]):
                        high = mid
                    else:
                        low = mid
                elif self.f(mid) > 0:
                    if self.f(signChangeRange[0]) < self.f(signChangeRange[1]):
                        high = mid
                    else:
                        low = mid
                else:
                    low = mid
                    high = mid
            roots.append(round(low, 6))
        return list(dict.fromkeys(roots))
    def getRoots(self):
        signChanges = self.getSignChanges()
        roots = []
        for signChange in signChanges:
            averageRoc = (self.f(round(signChange, 6) + 0.000001) - self.f(round(signChange, 6) - 0.000001)) / 0.000002
            instantRoc = Function(self.getFirstDerivative(), self.start, self.end).f(round(signChange, 6))
            if round(averageRoc, 3) == round(instantRoc, 3):
                roots.append(signChange)
        return roots
    def getCriticalNumbers(self):
        return Function(self.getFirstDerivative(), self.start, self.end).getSignChanges()
    def getInflectionPoints(self):
        return Function(self.getSecondDerivative(), self.start, self.end).getSignChanges()
    def getRightSlantAsympt(self):
        slopes = []
        for i in range(5, 10):
            slopes.append(round(Function(self.getFirstDerivative(), self.start, self.end).f(10 ** i), 2))
        if max(slopes) > min(slopes):
            return None
        straightenedAsympt = Function(self.funcExpr + " - " + str(max(slopes)) + " * x", self.start, self.end)
        asymptoteyInt = round(straightenedAsympt.f(10000000000), 2)
        return str(max(slopes)) + " * x + " + str(asymptoteyInt)
    def getLeftSlantAsympt(self):
        slopes = []
        for i in range(5, 10):
            slopes.append(round(Function(self.getFirstDerivative(), self.start, self.end).f(-(10 ** i)), 2))
        if max(slopes) > min(slopes):
            return None
        straightenedAsympt = Function(self.funcExpr + " - " + str(max(slopes)) + " * x", self.start, self.end)
        asymptoteyInt = round(straightenedAsympt.f(-10000000000), 2)
        return str(max(slopes)) + " * x + " + str(asymptoteyInt)
    def getVerticalAsymptotes(self):
        vertAsymptotes = []
        derivatives = [self.funcExpr]
        for i in range(3):
            derivatives.append(Function(derivatives[-1], self.start, self.end).getFirstDerivative())
        evenSignChanges = []
        oddSignChanges = []
        allSignChanges = []
        for i in range(len(derivatives)):
            print("--------------------------------------------", i + 1, "-------------------------------------------------")
            signChanges = Function(derivatives[i], self.start, self.end).getSignChanges()
            print(signChanges)
            if i % 2 == 1:
                oddSignChanges.append(signChanges)
            else:
                evenSignChanges.append(signChanges)
            allSignChanges += signChanges
        for signChange in allSignChanges:
            if False not in [(signChange in oddSignChange) for oddSignChange in oddSignChanges] or \
               False not in [(signChange in evenSignChange) for evenSignChange in evenSignChanges]:
                vertAsymptotes.append(signChange)
        return list(dict.fromkeys(vertAsymptotes))

#func = Function("x ** 2 - 6 * x + 5", -10, 10)
# No issues

#func = Function("(x ** 2 - 4) / (x ** 3 - 8)", -10, 10)
# No issues

#func = Function("math.sin(math.cos(x) + math.log(x, 10))", 0.001, 10)
# No issues

#func = Function("(x - 2) ** 3 - 2", -10, 10)
# No issues

#func = Function("-1 * ((12) / (11 * x - 3)) + 6", -30, 30)
# No issues

#func = Function("(((x - 2) * ((x + 5) ** 3)) * (x - 1)) / (((x + 1) * (x + 3)) * ((x - 3) * (x - 4)))", -10, 10)
# Roots - IROC Zero division error

#func = Function("(((7 * x - 2) * ((3 * x + 5) ** 3)) * (3 * x - 1)) / (((9 * x + 1) * (13 * x + 3)) * ((11 * x - 3) * (7 * x - 4)))", -10, 10)
# Third derivative inaccurate
# VA - 3rd derivative sign changes - slow
# Right/left slant asymptote - wrong y-int - big number

#func = Function("-1 * ((100 * x ** 3 - 6 * x + 3) / (50 * x ** 2 - 3 * x - 500)) + 5", -10, 10)
# VA - 3rd derivative sign changes - slow

#func = Function("math.log(x, 4) + (2 * x ** 2 - 100 * x + 1) / (2 * x)", 0.001, 30)
# VA - 3rd derivative sign changes - slow
# First derivative string - Case 6 - "DERIVATIVE1"

#func = Function("math.sin(x)", -10, 10)
# VA - incorrect - registers zeroes as VAs

func = Function("(12 * x ** 2 + 10 * x - 4) / (10 * x - 5)", -10, 10)
# Roots - IROC Zero division error
# VA - incorrect - registers zeroes as VAs
# First derivative string - Case 6 - "DERIVATIVE10"

#func = Function("(10 * x * math.log(x ** 2, 10)) / (x ** 2 + 2 * x - 8) - 2 * x + 8", 0.01, 10)
# Roots - IROC Zero division error
# Inflection points - slow
# VA - 2nd derivative sign changes - slow
# First derivative string - Case 6 - "DERIVATIVE1"

#func = Function("-1 * ((1) / (29 * x - 3)) + 6", -30, 30)
# VA - 3rd derivative sign changes - slow
# First derivative string - Case 6 - "DERIVATIVE1"

#func = Function("(1) / ((29 * x - 3) ** 2) + 6", -30, 30)
# VA - 3rd derivative sign changes - slow
# First derivative string - Case 6 - "DERIVATIVE1"

#func = Function("(50) / ((((3 * x - 2) ** 2) * ((3 * x + 4) ** 2)) * (2 * x + 7)) + 1", -30, 30)
# Roots - IROC Zero division error
# VA - 3rd derivative sign changes - slow
# First derivative string - Case 6 - "DERIVATIVE1"


print("f(x) =", func.funcExpr)
print()
#print("y-int:", func.getyInt())
#print()
fPrime = func.getFirstDerivative()
print("f'(x) =", fPrime)
print()
fDoublePrime = func.getSecondDerivative()
print("f''(x) =", fDoublePrime)
print()
fTriplePrime = Function(fDoublePrime, func.start, func.end).getFirstDerivative(1)
print("f'''(x) =", fTriplePrime)
print()
print("Sign changes:", func.getSignChanges())
print()
#print("Roots:", func.getRoots())
#print()
print("Critical numbers:", func.getCriticalNumbers())
print()
print("Inflection points:", func.getInflectionPoints())
print()
print("Right slant asymptote:", func.getRightSlantAsympt())
print()
#print("Left slant asymptote:", func.getLeftSlantAsympt())
#print()
print("Vertical asymptote:", func.getVerticalAsymptotes())

#canvas.mainloop()
