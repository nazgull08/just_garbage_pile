from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class OutputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabEMSRa = QWidget()
        self.tabEMSRb = QWidget()
        self.tabs.addTab(self.tabEMSRa, "EMSR-a")
        self.tabs.addTab(self.tabEMSRb, "EMSR-b")
        self.plotWidgets = {}
        self.addPlot(self.tabEMSRa, "График EMSR-a", "emsra")
        self.addPlot(self.tabEMSRb, "График EMSR-b", "emsrb")
        layout.addWidget(self.tabs)

    def addPlot(self, tab, title, plotId):
        plotLayout = QVBoxLayout()
        figure = Figure()
        canvas = FigureCanvas(figure)
        plotLayout.addWidget(canvas)
        tab.setLayout(plotLayout)
        self.plotWidgets[plotId] = (figure, canvas)

    def updateResults(self, dataA, dataB):
        # Обновление данных для EMSR-a
        figureA, canvasA = self.plotWidgets['emsra']
        axA = figureA.add_subplot(111)
        axA.clear()
        axA.bar(dataA.keys(), dataA.values(), color='blue')
        axA.set_title("Результаты EMSR-a")
        canvasA.draw()

        # Обновление данных для EMSR-b
        figureB, canvasB = self.plotWidgets['emsrb']
        axB = figureB.add_subplot(111)
        axB.clear()
        axB.bar(dataB.keys(), dataB.values(), color='green')
        axB.set_title("Результаты EMSR-b")
        canvasB.draw()
