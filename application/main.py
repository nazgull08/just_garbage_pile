import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QMenuBar, QAction, qApp, QFileDialog
from PyQt5.QtCore import Qt
from input_window import InputWindow
from output_window import OutputWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Меню
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('Файл')
        self.addFileMenuActions(fileMenu)

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

    def addFileMenuActions(self, menu):
        actions = {
            "Новый": self.newFile,
            "Открыть": self.openFile,
            "Сохранить": self.saveFile,
            "Выйти": self.exitApp
        }
        for name, func in actions.items():
            action = QAction(name, self)
            action.triggered.connect(func)
            menu.addAction(action)

    def newFile(self):
        print("Создание нового файла")

    def openFile(self):
        print("Открытие файла")

    def saveFile(self):
        print("Сохранение файла")

    def exitApp(self):
        qApp.quit()

        # Добавить в класс MainWindow:
    def newFile(self):
        self.inputWindow.clearTable()

    def openFile(self):
        # Запросите имя файла, например, через QFileDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "CSV файлы (*.csv)")
        if filename:
            self.inputWindow.loadTable(filename)

    def saveFile(self):
        # Запросите имя файла, например, через QFileDialog
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "CSV файлы (*.csv)")
        if filename:
            self.inputWindow.saveTable(filename)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
