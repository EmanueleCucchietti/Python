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
from mpl_interactions import ioff, panhandler, zoom_factory

from MainFuctions import *

# Global variables
PlotExpr = Plot()
FormMain = None
MainGroupBox = None
PlotGroupBox = None
TableGroupBox = None
TablePlot = None
Bisec = Bisection()
disconnect_zoom = None

def BtnBisezioneClick(Container, Table, EntryExpr, EntryXRangeMin, EntryXRangeMax, x_range, y_range, Error=0.01, isEqualAxis = True):
    # Clear the canvas
    print("bisec")
    for widget in Container.winfo_children():
        widget.destroy()
    # Clear the table
    Table.delete(*Table.get_children())
    # Get the expression, the lower bound, the upper bound and the error from the user
    # Display the expression in the plot and create the table using the expression and the bounds
    fig, plt = PlotExpr._createFigureAndPlot(container=Container, draw_axes=True, pure_expr=EntryExpr, x_range=x_range, y_range=y_range, isEmptyPlot=False, isEqualAxis=isEqualAxis)
    disconnect_zoom = zoom_factory(plt)
    expr = sp.sympify(EntryExpr)
    # Draw verical lines in the plot to indicate the bounds
    plt.axvline(x=float(EntryXRangeMin), color='r')
    plt.axvline(x=float(EntryXRangeMax), color='r')

    # Execute the bisection method and get the results in a list
    sequence = Bisec.evaluateSequence(expr, float(EntryXRangeMin), float(EntryXRangeMax), float(Error))
    # Display the results in the table
    for i in range(len(sequence)):
        Table.insert("", "end", 
            values=(
            ('%f' % sequence[i]["n"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["a"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["fa"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["b"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["fb"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["m"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["fm"]).rstrip('0').rstrip('.'),
            ('%f' % sequence[i]["err"]).rstrip('0').rstrip('.')
        ))

def main():
    # Create the main window
    # The main windows contains a labelframe
    # The labelframe contains contains 4 labels and 4 entry
    FormMain = Tk()
    FormMain.title("Plot Math Function")
    FormWidth = 1000*2
    TableWidth = (7.5/10)/4 * FormWidth
    FormHeight = 600
    FormMain.geometry()

    MainGroupBox = LabelFrame(FormMain, text="Plot Math Function")
    MainGroupBox.grid(row=0, column=0)
    
    # The labelframe contains contains 4 labels and 4 entry
    # The first label and entry are used to set the expression
    # The second label and entry are used to set the range of the x axis
    # The third label and entry are used to set the range of the y axis
    # The fourth label and entry are used to set the number of points between each x value
    # Labels and entries are contained in a frame

    InputGroupBox = LabelFrame(MainGroupBox, text="Input")
    InputGroupBox.grid(row=0, column=0, columnspan=2, padx=5)

    LabelExpr = Label(InputGroupBox, text="Expression")
    LabelExpr.grid(row=0, column=0)
    EntryExpr = Entry(InputGroupBox)
    EntryExpr.grid(row=0, column=1)

    LabelXRangeMin = Label(InputGroupBox, text="Min Range X")
    LabelXRangeMin.grid(row=1, column=0)
    EntryXRangeMin = Entry(InputGroupBox)
    EntryXRangeMin.grid(row=1, column=1)

    LabelXRangeMax = Label(InputGroupBox, text="Max Range X")
    LabelXRangeMax.grid(row=2, column=0)
    EntryXRangeMax = Entry(InputGroupBox)
    EntryXRangeMax.grid(row=2, column=1)

    LabelPrecision = Label(InputGroupBox, text="Points between each x value")
    LabelPrecision.grid(row=3, column=0)
    EntryPrecision = Entry(InputGroupBox)
    EntryPrecision.grid(row=3, column=1)

    # RangePlotGroupBox contains 4 labels and 4 entry to set the left and right bounds of the plot
    # The first and second label and entry are used to set the left and right bound of the plot in the x axis 
    # The third and fourth label and entry are used to set the left and right bound of the plot in the y axis

    # The entries default values are set to -10 and 10
    RangePlotGroupBox = LabelFrame(MainGroupBox, text="Range Plot")
    RangePlotGroupBox.grid(row=1, column=0, columnspan=2, padx=5)

    LabelXRangePlotMin = Label(RangePlotGroupBox, text="Min Range X")
    LabelXRangePlotMin.grid(row=0, column=0)
    EntryXRangePlotMin = Entry(RangePlotGroupBox)
    EntryXRangePlotMin.grid(row=0, column=1)
    EntryXRangePlotMin.insert(0, "-10")

    LabelXRangePlotMax = Label(RangePlotGroupBox, text="Max Range X")
    LabelXRangePlotMax.grid(row=1, column=0)
    EntryXRangePlotMax = Entry(RangePlotGroupBox)
    EntryXRangePlotMax.grid(row=1, column=1)
    EntryXRangePlotMax.insert(0, "10")

    # ButtonGroupBox contains the button to plot the function
    ButtonGroupBox = LabelFrame(InputGroupBox, text="", border=0)
    ButtonGroupBox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # The labelframe contains a button to plot the function
    ButtonBisection = Button(ButtonGroupBox, text="Bisection",
                                            command = lambda: BtnBisezioneClick(PlotGroupBox, TablePlot, EntryExpr.get(), EntryXRangeMin.get(), EntryXRangeMax.get(),[float(EntryXRangePlotMin.get()),float(EntryXRangePlotMax.get())],[], EntryPrecision.get(), True))
    ButtonBisection.grid(row=0, column=0, padx=5)

    # The labelframe contains a button to clear the canvas
    ButtonClear = Button(ButtonGroupBox, text="Clear")
    ButtonClear.grid(row=0, column=1, padx=5)
    # clear the canvas
    ButtonClear.bind("<Button-1>", lambda event: PlotExpr._clearCanvas())

    # The labelframe contains another sub labelframe
    # The sub labelframe contains a canvas to plot the expression and a table to show the sequence of the bisection method
    # The table is positioned on the bottom of the canvas and has the same width of the canvas
    # The total height of the sub labelframe is the same of the main labelframe
    # The sub labelframe is wrapped in the main labelframe
    SubGroupBox = LabelFrame(MainGroupBox, text="Data", width=TableWidth*3, height=FormHeight)
    SubGroupBox.grid(row=0, column=2, rowspan=5)

    # Create labelframe containing the canvas
    PlotGroupBox = LabelFrame(SubGroupBox, text="", border=0)
    PlotGroupBox.grid(row=0, column=0)
    # the canvas contains the plot
    # the plot is created using the matplotlib library
    # the plot is wrapped in the canvas
    # the plot is created using the Plot class
    # temporary create empty plot
    PlotExpr._createFigureAndPlot(container=PlotGroupBox, draw_axes=True, pure_expr="x**2", x_range=[-200, 200], y_range=[], isEmptyPlot=True, isEqualAxis=True)



    # Create the table
    TablePlot = ttk.Treeview(SubGroupBox)
    TablePlot.grid(row=1, column=0)
    Headings = ["n", "a", "f(a)", "b", "f(b)", "m", "f(m)", "Error"]
    TablePlot["columns"] = Headings
    TablePlot["show"] = "headings"
    for Heading in Headings:
        TablePlot.heading(Heading, text=Heading)
        TablePlot.column(Heading, width=int(TableWidth/8*3))


    FormMain.mainloop()

main()