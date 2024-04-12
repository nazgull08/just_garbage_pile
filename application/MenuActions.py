# MenuActions.py

from PyQt5.QtWidgets import QAction, QFileDialog, qApp

class MenuActions:
    def __init__(self, main_window, menu):
        self.main_window = main_window
        self.addFileMenuActions(menu)

    def addFileMenuActions(self, menu):
        # Определение действий меню
        actions = {
            "Новый": self.newFile,
            "Открыть": self.openFile,
            "Сохранить": self.saveFile,
            "Выйти": self.exitApp
        }
        for name, func in actions.items():
            action = QAction(name, self.main_window)
            action.triggered.connect(func)
            menu.addAction(action)

    def newFile(self):
        self.main_window.inputWindow.clearTable()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self.main_window, "Открыть файл", "", "CSV файлы (*.csv)")
        if filename:
            self.main_window.inputWindow.loadTable(filename)

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self.main_window, "Сохранить файл", "", "CSV файлы (*.csv)")
        if filename:
            self.main_window.inputWindow.saveTable(filename)

    def exitApp(self):
        qApp.quit()
