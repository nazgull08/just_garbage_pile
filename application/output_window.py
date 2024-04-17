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
        ax = figure.add_subplot(111)
        ax.set_title(title)
        plotLayout.addWidget(canvas)
        tab.setLayout(plotLayout)
        self.plotWidgets[plotId] = (figure, canvas, ax)

    def updateResults(self, dataA, dataB):
        # Обновление данных для EMSR-a
        figureA, canvasA, axA = self.plotWidgets['emsra']
        axA.clear()
        barsA = axA.bar(dataA.keys(), dataA.values(), color='blue')
        axA.set_title("Результаты EMSR-a")
        # Добавление текстовых подписей к столбцам с округлением до двух десятичных знаков
        for bar in barsA:
            height = bar.get_height()
            axA.text(bar.get_x() + bar.get_width() / 2, height, f'{round(height, 2)}', ha='center', va='bottom')
        canvasA.draw()

        # Обновление данных для EMSR-b
        figureB, canvasB, axB = self.plotWidgets['emsrb']
        axB.clear()
        barsB = axB.bar(dataB.keys(), dataB.values(), color='green')
        axB.set_title("Результаты EMSR-b")
        # Добавление текстовых подписей к столбцам с округлением до двух десятичных знаков
        for bar in barsB:
            height = bar.get_height()
            axB.text(bar.get_x() + bar.get_width() / 2, height, f'{round(height, 2)}', ha='center', va='bottom')
        canvasB.draw()
