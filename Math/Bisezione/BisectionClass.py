import sympy as sp
from sympy import zoo, oo, nan
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Bisection:
    
    def f(self, expr, xValue):
        #Evaluate a mathematical expression with a given value for x and return the result as a float
        
        x = sp.symbols("x")
        f = sp.N(expr.subs(x, xValue))
        if(f.has(oo, -oo, zoo, nan)): f = np.nan
        return f

    def getMvalue(self, expr, a, b):
        #Get the value of the middle point between a and b
        return (a + b) / 2

    def getNewInterval(self, expr, a, b):
        #Get the new interval based on the value of the middle point between a and b
        m = self.getMvalue(expr, a, b)
        if(self.f(expr, m) * self.f(expr, a) < 0): return a, m
        else: return m, b

    def evaluateSequence(self, expr, a, b, error):
        #Evaluate the sequence of the bisection method
        #Return the list of the middle points and return array of {"a": a, "fa": self.f(expr, a), "b": b, "fb": self.f(expr, b), "m": m, "fm": self.f(expr, m), "err": abs(b - a)/2}
        m = self.getMvalue(expr, a, b)
        sequence = []
        i=0
        sequence.append({"n": i, "a": a, "fa": self.f(expr, a), "b": b, "fb": self.f(expr, b), "m": m, "fm": self.f(expr, m), "err": abs(b - a)/2})
        while(abs(b - a)/2 > error and not self.f(expr, m) == 0):
            a, b = self.getNewInterval(expr, a, b)
            m = self.getMvalue(expr, a, b)
            sequence.append({"n": i, "a": a, "fa": self.f(expr, a), "b": b, "fb": self.f(expr, b), "m": m, "fm": self.f(expr, m), "err": abs(b - a)/2})
            i+=1
        return sequence
# 
# pure_expr = input("Enter the expression: ")
# x = sp.symbols("x")
# expr = sp.sympify(pure_expr)
# a = float(input("Enter the lower bound: "))
# b = float(input("Enter the upper bound: "))
# error = float(input("Enter the error: "))
# bisec = Bisection()
# sequence = bisec.evaluateSequence(expr, a, b, error)
# for i in sequence: print(i)