import sympy as sp
from sympy import zoo, oo, nan
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from BisectionClass import Bisection

pure_expr = input("Enter the expression: ")
x = sp.symbols("x")
expr = sp.sympify(pure_expr)
a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))
error = float(input("Enter the error: "))
bisec = Bisection()
sequence = bisec.evaluateSequence(expr, a, b, error)
for i in sequence: print(i)