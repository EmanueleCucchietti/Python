from tkinter import *
from sympy import symbols, sympify
import sympy as sp
from mpmath import radians
from matplotlib import pyplot as plt

ax = []
ay = []

def EvaluateFunction(expr, XActualValue):
    #Evaluate a mathematical expression with a given value for x and return the result as a float
    s = sp.N(expr.subs(x, XActualValue))

def GetOneHundredCoordinates(expr):
    #Get a list of 100 x,y coordinates for a given expression
    ax = []
    ay = []
    x = symbols("x")
    for i in range(0,100):
        f = sp.N(expr.subs(x, i))
        ax.append(i) 
        ay.append(f)
    return ax, ay

def PlotFunction(ax, ay):
    #Plot a function given a list of x,y coordinates
    plt.plot(ax, ay)
    plt.show()

def main():
    x = symbols("x")
    IsRadians = True
    XPreValue = 3
    XActualValue = None
    if(IsRadians):
        XActualValue = XPreValue
    else:
        XActualValue = radians(XPreValue)

    expr2 = "x^5  + 3*x + 5"
    expr = sympify(expr2)
    ax, ay = GetOneHundredCoordinates(expr)
    PlotFunction(ax, ay)


screen = Tk()
screen.title("Plot Math Function")
screen.geometry("500x500")
heading = Label(screen, text="Plot Math Function", font=("Arial", 20))
heading.pack()

TxtFunction = Entry(screen, width=50)
TxtFunction.pack()

def Plot():
    expr2 = TxtFunction.get()
    expr = sympify(expr2)
    ax, ay = GetOneHundredCoordinates(expr)
    PlotFunction(ax, ay)

BtnPlot = Button(screen, text="Plot", command=Plot)
BtnPlot.pack()

screen.mainloop()

