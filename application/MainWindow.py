
# MainWindow.py

from PyQt5.QtWidgets import QMainWindow, QSplitter, QAction, qApp, QFileDialog
from PyQt5.QtCore import Qt
from input_window import InputWindow
from output_window import OutputWindow
from MenuActions import MenuActions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создание и настройка меню
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('Файл')
        self.menuActions = MenuActions(self, fileMenu)

        # Основной разделитель главного окна
        splitter = QSplitter(Qt.Vertical)
        self.setCentralWidget(splitter)

        # Верхняя панель: окно ввода
        self.inputWindow = InputWindow()
        splitter.addWidget(self.inputWindow)

        # Нижняя панель: окно вывода
        self.outputWindow = OutputWindow()
        splitter.addWidget(self.outputWindow)

        # Настройки окна
        self.setWindowTitle('EMSR Analysis Tool')
        self.setGeometry(200, 100, 800, 600)
        self.show()
