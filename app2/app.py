import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSlider, QLabel,
                             QVBoxLayout, QHBoxLayout, QWidget, QAction,
                             QFileDialog, QGraphicsView, QGraphicsScene)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Создание действий меню
        openAction = QAction('Открыть', self)
        openAction.triggered.connect(self.openFile)
        
        saveAction = QAction('Сохранить', self)
        saveAction.triggered.connect(self.saveFile)
        
        exitAction = QAction('Выход', self)
        exitAction.triggered.connect(self.close)
        
        # Создание строки меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
        
        # Создание ползунков
        slider1 = QSlider(Qt.Horizontal, self)
        slider1.setMinimum(1)
        slider1.setMaximum(100)
        slider1.setValue(50)
        
        slider2 = QSlider(Qt.Horizontal, self)
        slider2.setMinimum(1)
        slider2.setMaximum(100)
        slider2.setValue(50)
        
        # Вертикальное размещение ползунков
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(slider1)
        leftLayout.addWidget(slider2)
        
        # Создание просмотрщика изображений
        self.viewer = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.viewer.setScene(self.scene)
        
        # Горизонтальное размещение виджетов
        centralLayout = QHBoxLayout()
        centralLayout.addLayout(leftLayout, 1)
        centralLayout.addWidget(self.viewer, 5)
        
        # Установка центрального виджета
        centralWidget = QWidget(self)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)
        
        # Настройка окна
        self.setWindowTitle('PyQt Программа')
        self.setGeometry(100, 100, 800, 600)
        
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Открыть изображение", 
                                                  "", "Image Files (*.png *.jpg *.bmp)")
        if fileName:
            pixmap = QPixmap(fileName)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.viewer.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)
    
    def saveFile(self):
        print("Функция сохранения файла")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
