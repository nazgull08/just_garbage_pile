from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class OutputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Текстовый вывод
        self.textOutput = QTextEdit()
        layout.addWidget(self.textOutput)

        # Вкладки для разных методов и их графиков
        self.tabs = QTabWidget()
        self.tabLittlewood = QWidget()
        self.tabEMSRa = QWidget()
        self.tabEMSRb = QWidget()

        # Добавление вкладок
        self.tabs.addTab(self.tabLittlewood, "Littlewood")
        self.tabs.addTab(self.tabEMSRa, "EMSR-a")
        self.tabs.addTab(self.tabEMSRb, "EMSR-b")

        # Добавление графиков в каждую вкладку
        self.addPlot(self.tabLittlewood, "График Littlewood")
        self.addPlot(self.tabEMSRa, "График EMSR-a")
        self.addPlot(self.tabEMSRb, "График EMSR-b")

        layout.addWidget(self.tabs)

    def addPlot(self, tab, title):
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.set_title(title)
        ax.plot([0, 1, 2, 3], [0, 1, 0, 1])  # Пример данных
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        tab.setLayout(layout)

        # Обновляем интерфейс с графиком
