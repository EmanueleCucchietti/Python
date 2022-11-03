from BisectionClass import Bisection

def BtnBisezioneClick(PlotContainer, TableContainer, EntryExpr, EntryXRange, EntryYRange, EntryInUnitValues):
    myPlot = Plot()
    myPlot._createFigureAndPlot(PlotGroupBox, True, "x", [-100, 100], True)