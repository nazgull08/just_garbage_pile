from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class OutputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Вкладки для разных методов и их графиков
        self.tabs = QTabWidget()
        self.tabLittlewood = QWidget()
        self.tabEMSRa = QWidget()
        self.tabEMSRb = QWidget()

        # Добавление вкладок
        self.tabs.addTab(self.tabLittlewood, "Littlewood")
        self.tabs.addTab(self.tabEMSRa, "EMSR-a")
        self.tabs.addTab(self.tabEMSRb, "EMSR-b")

        # Создаем словарь для хранения элементов графика и текста для каждой вкладки
        self.plotWidgets = {}
        self.addPlot(self.tabLittlewood, "График Littlewood", "littlewood")
        self.addPlot(self.tabEMSRa, "График EMSR-a", "emsra")
        self.addPlot(self.tabEMSRb, "График EMSR-b", "emsrb")

        layout.addWidget(self.tabs)

    def addPlot(self, tab, title, key):
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.set_title(title)
        ax.plot([], [])  # Пример данных
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        tab.setLayout(layout)
        self.plotWidgets[key] = (canvas, ax, fig)  # Сохраняем ссылки на компоненты графика

    def updateResults(self, prices_lw, protected_seats_lw, prices_em, protected_seats_a, emsrb_revenue):
        # Обновляем данные для вкладки Littlewood
        canvas_lw, ax_lw, fig_lw = self.plotWidgets["littlewood"]
        ax_lw.clear()
        ax_lw.bar(prices_lw, protected_seats_lw, color='red')
        ax_lw.set_title("Защищенные места по Littlewood")
        ax_lw.set_xlabel("Цены")
        ax_lw.set_ylabel("Защищенные места")
        fig_lw.canvas.draw()

        # Обновляем данные для вкладки EMSR-a
        canvas_a, ax_a, fig_a = self.plotWidgets["emsra"]
        ax_a.clear()
        ax_a.bar(prices_em, protected_seats_a, color='green')
        ax_a.set_title("Защищенные места по EMSR-a")
        ax_a.set_xlabel("Цены")
        ax_a.set_ylabel("Защищенные места")
        fig_a.canvas.draw()

        # Обновляем данные для вкладки EMSR-b
        canvas_b, ax_b, fig_b = self.plotWidgets["emsrb"]
        ax_b.clear()
        if len(prices_em) == len(emsrb_revenue):
            ax_b.bar(prices_em, emsrb_revenue, color='blue')
        else:
            print(f"Data length mismatch: prices ({len(prices_em)}), revenue ({len(emsrb_revenue)})")
        ax_b.set_title("Ожидаемые доходы по EMSR-b")
        ax_b.set_xlabel("Цены")
        ax_b.set_ylabel("Ожидаемый доход")
        fig_b.canvas.draw()
