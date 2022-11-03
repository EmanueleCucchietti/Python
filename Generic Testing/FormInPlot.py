from tkinter import *
from sympy import symbols, sympify
from sympy import zoo, oo, nan
import sympy as sp
import numpy as np
from mpmath import radians
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from mpl_interactions import ioff, panhandler, zoom_factory
from PlotClass import Plot

def EvaluateFunction(expr, XActualValue):
    #Evaluate a mathematical expression with a given value for x and return the result as a float
    s = sp.N(expr.subs(x, XActualValue))

def GetCoordinates(expr, x0, x1, inUnitValues = 10):
    # inUnitValues indicates how many numbers are between each x value
    #Get a list of 100 x,y coordinates for a given expression
    ax = []
    ay = []
    x = symbols("x")
    arrayX = [0,*np.linspace(x0, x1, (x1-x0)*inUnitValues)]
    arrayX.sort()
    # the problem in tan function an similar is that the plot is not continuous, so it won't plot the points where the function doesn't exist
    # thus, there aren't nan values in the array, so the plot will be continuous and the points where the function doesn't exist will be connected with a straight line
    # to resolve the problem and plot the points where the function doesn't exist, we need to check if the function is continuous in the given range
    # if it is, we can plot the points where the function doesn't exist
    # to check if the function exist in a given range, we need to check if the function is continuous in the given range
    # if it is, we can plot the points where the function doesn't exist
    for i in arrayX:
        f = sp.N(expr.subs(x, i))
        if(f.has(oo, -oo, zoo, nan)):
            f = np.nan
        if(len(ay) != 0 and ay[-1] == nan):
            ay.append(np.nan)
        else:
            ay.append(f)
        ax.append(i)
    return ax, ay

def _createFigureAndPlot(container, draw_axes, pure_expr, x_range):
    # Create a figure and a subplot with a single plot, based on draw_axes parameter draws the x and y axis
    # use the pure_expr parameter to plot the expression
    # use the x_range parameter to set the range of the x axis
    # doesn't use pack(), it uses grid() to place the canvas in the container
    
    # doesn't return anything because it plots the figure directly in the container's canvas
    fig = Figure(figsize = (5, 5), dpi = 100)
    with plt.ioff():
        plot1 = fig.add_subplot(111)
    plot1.grid()
    plot1.set_xlim(x_range)
    plot1.set_ylim([-100, 100])
    

    if(draw_axes):
        # Creates the x and y axis
        plot1.axvline(x=0, c="black", label="x=0")
        plot1.axhline(y=0, c="black", label="y=0")

    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = container)  
    canvas.draw()

    # placing the canvas on the Tkinter window
    lastRow, lastColumn = container.grid_size()
    canvas.get_tk_widget().grid(row = lastRow, column = 0)

    # creating the Matplotlib toolbar
    toolbarFrame = Frame(master = container)
    toolbarFrame.grid(row = lastRow+1, column = 0)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row = lastRow, column = 0)

    # Plot the expression
    ax, ay = GetCoordinates(sympify(pure_expr), x_range[0], x_range[1])
    # print ay values if it's convertible to float
    ayFloated = []
    for i in ay:
        try:
            ayFloated.append(float(i))
        except:
            ayFloated.append(nan)
    plot1.plot(ax, ayFloated)
    disconnect_zoom = zoom_factory(plot1)

# main function

ax = []
ay = []

FormMain = Tk()
Plot = Plot()
FormMain.title("Plot Math Function")
FormMain.geometry("700x700")

MainGroupBox = LabelFrame(FormMain, text="Plot Math Function")
MainGroupBox.grid(row=0, column=0, padx=5, pady=5)

heading = Label(MainGroupBox, text="Plot Math Function", font=("Arial", 20))
heading.grid(row=0, column=0, columnspan=2, pady=10)

TxtFunction = Entry(MainGroupBox, width=50)
TxtFunction.grid(row=1, column=0, padx=10, pady=10)


BtnPrintPlot = Button(master = MainGroupBox, 
                     command = lambda: Plot._createFigureAndPlot(MainGroupBox, True, TxtFunction.get(), [-100, 100]),
                     height = 2, 
                     width = 10,
                     text = "Plot")
BtnPrintPlot.grid(row=1, column=1, padx=10, pady=10)



FormMain.mainloop()