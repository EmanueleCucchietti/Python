from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
from sympy import zoo, oo, nan, symbols, N, sympify
import sympy as sp
import numpy as np
from mpl_interactions import ioff, panhandler, zoom_factory

class Plot:
    def __init__(self):
        fig = None;
        plot1 = None;

    def GetCoordinates(self, expr, x0, x1, inUnitValues = 0.01):
        # inUnitValues indicates how many numbers are between each x value
        #Get a list of 100 x,y coordinates for a given expression
        ax = []
        ay = []
        x = symbols("x")
        arrayX = [0,*np.arange(x0, x1, inUnitValues)]
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

    def _createFigureAndPlot(self, container, draw_axes, pure_expr, x_range, y_range, isEmptyPlot = False, isEqualAxis = True):
        # Create a figure and a subplot with a single plot, based on draw_axes parameter draws the x and y axis
        # use the pure_expr parameter to plot the expression
        # use the x_range parameter to set the range of the x axis
        # doesn't use pack(), it uses grid() to place the canvas in the container
        # doesn't return anything because it plots the figure directly in the container's canvas
        if isEqualAxis:
            y_range = x_range

        # empty the container
        for widget in container.winfo_children():
            widget.destroy()

        fig = Figure(figsize = (5, 5), dpi = 100)
        fig.set_size_inches(10, 5)
        with plt.ioff():
            plot1 = fig.add_subplot(111)
        plot1.grid()
        plot1.set_xlim(x_range)
        plot1.set_ylim(y_range)
        
    
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
        if(not isEmptyPlot):

            ax, ay = self.GetCoordinates(sympify(pure_expr), x_range[0], x_range[1])
            # print ay values if it's convertible to float
            ayFloated = []
            for i in ay:
                try:
                    ayFloated.append(float(i))
                except:
                    ayFloated.append(nan)
        else:
            ax = []
            ayFloated = []
        plot1.plot(ax, ayFloated)
        # disconnect_zoom = zoom_factory(plot1)
        return fig, plot1

    def _clearCanvas(self, container):
        plot1.clf()