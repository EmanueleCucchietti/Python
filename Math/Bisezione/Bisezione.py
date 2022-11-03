from BisectionClass import Bisection
from PlotClass import Plot
import tkinter as tk
from tkinter import ttk

import sympy as sp
from sympy import zoo, oo, nan
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

"""
    The Following software does the following:
    1. It takes the expression, the lower bound, the upper bound and the error as input from the user
    2. It evaluates the sequence of the bisection method
    3. Prints the sequence into a table on tkinter window
    4. Plots the graph of the function
"""

def main():
    #Get the expression, the lower bound, the upper bound and the error from the user
    # pure_expr = input("Enter the expression: ")

    ax = []
    ay = []

    pure_expr = "x+1"
    expr = sp.sympify(pure_expr)
    # a = float(input("Enter the lower bound: "))
    a = -400
    # b = float(input("Enter the upper bound: "))
    b = +200
    # error = float(input("Enter the error: "))
    error = 0.000001
    #Create an instance of the Bisezione class
    bisec = Bisection()
    #Evaluate the sequence of the bisection method
    sequence = bisec.evaluateSequence(expr, a, b, error)
    

    ax = []
    ay = []

    FormMain = Tk()
    FormMain.title("Plot Math Function")
    FormWidth = 1000*2
    TableWidth = (7.5/10)/2 * FormWidth
    FormHeight = 600
    FormMain.geometry(f"{FormWidth}x{FormHeight}")

    MainGroupBox = LabelFrame(FormMain, text="Plot Math Function")
    MainGroupBox.grid(row=0, column=0)

    heading = Label(MainGroupBox, text="Function:", font=("Arial", 12))
    heading.grid(row=0, column=0, columnspan=1, pady=4)
    heading = Label(MainGroupBox, text="Intervallo A", font=("Arial", 12))
    heading.grid(row=0, column=1, columnspan=1, pady=4)
    heading = Label(MainGroupBox, text="Intervallo B", font=("Arial", 12))
    heading.grid(row=0, column=2, columnspan=1, pady=4)
    heading = Label(MainGroupBox, text="Precisione", font=("Arial", 12))
    heading.grid(row=0, column=3, columnspan=1, pady=4)

    TxtFunction = Entry(MainGroupBox, width=20)
    TxtFunction.grid(row=1, column=0, padx=3, pady=4)
    TxtFunction = Entry(MainGroupBox, width=20)
    TxtFunction.grid(row=1, column=1, padx=3, pady=4)
    TxtFunction = Entry(MainGroupBox, width=20)
    TxtFunction.grid(row=1, column=2, padx=3, pady=4)
    TxtFunction = Entry(MainGroupBox, width=20)
    TxtFunction.grid(row=1, column=3, padx=3, pady=4)


    # Draw the graph
    # on the canvas positioned on the main window, right side of the table
    myPlot = Plot()
    PlotGroupBox = LabelFrame(MainGroupBox, text="Plot")
    PlotGroupBox.grid(row=3, column=1, padx=10, pady=10)
    myPlot._createFigureAndPlot(PlotGroupBox, True, "x", [-100, 100], True)
    BtnPrintPlot = Button(master = MainGroupBox, 
                         command = lambda: myPlot._createFigureAndPlot(PlotGroupBox, True, TxtFunction.get(), [-100, 100]),
                         height = 2, 
                         width = 10,
                         text = "Plot")
    BtnPrintPlot.grid(row=1, column=1, padx=10, pady=10)

    print(FormMain.winfo_width())
    table = ttk.Treeview(MainGroupBox,columns=(1,2,3,4,5,6,7,8), show="headings", height="6")
    table.column("# 1", width=25, minwidth=25, stretch="YES",)
    table.heading("# 1", text="n")
    TableWidth -= 25
    for i, key in enumerate(sequence[0].keys()):
        print(i+1)
        table.column(f"# {i+2}", width=int(TableWidth/7), minwidth=50, stretch="YES", )
        table.heading(f"# {i+2}", text=key)
    #Add the sequence to the table
    for i in range(len(sequence)):
        table.insert("", "end", 
            values=((i+1),
            ('%f' % sequence[i]["a"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["fa"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["b"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["fb"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["m"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["fm"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["err"]).rstrip('0').rstrip('.'),
        ))
    table.grid(row=3, column=0)


    FormMain.mainloop()


main()