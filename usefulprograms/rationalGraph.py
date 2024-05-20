#! /usr/bin/python3

import math

class Rational:
    def __init__(self, numTerms, denTerms):
        # terms of polynomial in numerator
        self.numTerms = numTerms
        # terms of polynomial in denominator
        self.denTerms = denTerms
        # horizontal asymptote
        self.horizAsympt = None
        # oblique asymptote
        self.obliqueAsympt = []
        # vertical asymptote
        self.vertAsympt = []
        # vertical and horizontal limits
        self.vertLimits = []
        self.horizLimits = []
        # holes
        self.holes = []
    def setHA(self): # set horizontal asymptote
        print("setHA")
        if len(self.numTerms) < len(self.denTerms):
            # if denominator has higher degree, horizontal asymptote = 0
            self.horizAsympt = 0
            print("Horizontal")
            print(self.horizAsympt)
        elif len(self.numTerms) == len(self.denTerms):
            # if numerator and denominator have same degree, divide leading coefficients
            self.horizAsympt = self.numTerms[0]/self.denTerms[0]
            print("Horizontal")
            print(self.horizAsympt)
        else:
            # if numerator has higher degree, oblique asymptote = num/den without the remainder
            self.obliqueAsympt = [0]*len(self.numTerms)
            tempNum = self.numTerms[:]
            idx = 0
            for x in range(len(self.numTerms)-len(self.denTerms)+1):
                print(tempNum[idx]/self.denTerms[0])
                self.obliqueAsympt[len(tempNum)-len(self.denTerms)+idx] = tempNum[idx]/self.denTerms[0]
                #for y in range(idx, idx+len(self.denTerms)):
                #    tempNum[y] -= self.obliqueAsympt[len(tempNum)-len(self.denTerms)+idx]*self.denTerms[y-idx]
                idx += 1
            #for x in range(len(self.numTerms)-len(self.denTerms)):
            #    self.obliqueAsympt.pop(0)
            print("Oblique")
            print(self.obliqueAsympt)
    def factors(self, number):
        f = []
        for x in range(1, math.ceil(math.sqrt(number))+1):
            if number/x == int(number/x):
                f.append(x)
                if x != number/x:
                    f.append(number/x)
        return f
    def rationalRoots(self, lead, const):
        possibleZeros = []
        for x in range(1, const+1):
            for y in range(1, lead+1):
                if const/x == int(const/x):
                    if lead/y == int(lead/y):
                        possibleZeros.append([x, y])
        remIdx = []
        for x in range(len(possibleZeros)):
            if possibleZeros[x][0] != 1:
                for y in self.factors(possibleZeros[x][0]):
                    if y in self.factors(possibleZeros[x][1]) and y != 1:
                        remIdx.append(x)
        possibleZeros = [possibleZeros[x] for x in range(len(possibleZeros)) if x not in remIdx]
        absZeroLen = len(possibleZeros)
        possibleZeros += [[-possibleZeros[x][0], possibleZeros[x][1]] for x in range(absZeroLen)]
        return possibleZeros
    def polyEval(self, poly, x, n):
        y = sum([poly[i]*x**(len(poly)-i-1) for i in range(len(poly))])
        if n:
            for i in range(len(poly)):
                print(poly[i], x, len(poly)-i-1, poly[i]*x**(len(poly)-i-1))
        return y
    def setVA(self):
        print("setVA")
        ratRoots = self.rationalRoots(self.denTerms[0], self.denTerms[-1])
        for x in ratRoots:
            if self.polyEval(self.denTerms, x[0]/x[1], False) == 0:
                self.vertAsympt.append(x)
        print(self.vertAsympt)
        if len(self.vertAsympt)+2 < len(self.denTerms)-1:
            print("Error")
        elif len(self.vertAsympt)+2 == len(self.denTerms)-1:
            print("Quad formula")
        else:
            print("All rational")
        # Factor denominator
        # Set vert asympt to zeros

f = Rational([3, 1, 8], [2, 5, -2])
f.setHA()
g = Rational([1, -7], [1, 2, 4])
g.setHA()
h = Rational([1, -3, 6, -6], [3, -8])
h.setHA()
