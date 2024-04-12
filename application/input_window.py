import csv
from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QPushButton, QVBoxLayout, QMessageBox, QFileDialog
from littlewood import calculate_littlewood
from emsrb import calculate_emsr

class InputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout(self)

        # Таблица для данных
        self.table = QTableWidget(0, 4)  # Начально таблица без строк
        self.table.setHorizontalHeaderLabels(['Название класса', 'Цена', 'Спрос', 'Вероятность'])
        layout.addWidget(self.table, 0, 0, 5, 1)  # Занимает большую часть слева

        # Правая колонка для ввода данных и кнопок
        rightLayout = QVBoxLayout()

        # Ввод количества мест
        seatsLabel = QLabel('Количество мест:')
        self.seatsInput = QLineEdit()
        rightLayout.addWidget(seatsLabel)
        rightLayout.addWidget(self.seatsInput)

        # Ввод количества броней
        bookingsLabel = QLabel('Количество броней:')
        self.bookingsInput = QLineEdit()
        rightLayout.addWidget(bookingsLabel)
        rightLayout.addWidget(self.bookingsInput)

        # Кнопка для добавления тарифа
        self.addButton = QPushButton('Добавить тариф')
        self.addButton.clicked.connect(self.addTableRow)
        rightLayout.addWidget(self.addButton)

        # Кнопка для удаления тарифа
        self.deleteButton = QPushButton('Удалить тариф')
        self.deleteButton.clicked.connect(self.deleteTableRow)
        rightLayout.addWidget(self.deleteButton)

        # Добавление правой колонки в основной лейаут
        layout.addLayout(rightLayout, 0, 1, 5, 1)

        self.calculateButton = QPushButton("Посчитать", self)
        self.calculateButton.clicked.connect(self.calculate)
        layout.addWidget(self.calculateButton, 3, 1)

    def addTableRow(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

    def deleteTableRow(self):
        currentRow = self.table.currentRow()
        if currentRow != -1:
            self.table.removeRow(currentRow)

    def saveTable(self, filename='table.csv'):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
            QMessageBox.information(self, "Сохранение", "Данные успешно сохранены в " + filename)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Проблема при сохранении файла: " + str(e))

    def loadTable(self, filename='table.csv'):
        try:
            with open(filename, 'r', newline='') as file:
                self.table.setRowCount(0)
                reader = csv.reader(file)
                for row_data in reader:
                    row = self.table.rowCount()
                    self.table.insertRow(row)
                    for column, data in enumerate(row_data):
                        item = QTableWidgetItem(data)
                        self.table.setItem(row, column, item)
            QMessageBox.information(self, "Загрузка", "Данные успешно загружены из " + filename)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Проблема при загрузке файла: " + str(e))

    def clearTable(self):
        self.table.setRowCount(0)

    def calculate(self):
        prices = []
        mean = []
        sigma = []
        mest = 0

        # Извлечение данных из таблицы
        for row in range(self.table.rowCount()):
            prices.append(int(self.table.item(row, 1).text()))
            mean.append(float(self.table.item(row, 2).text()))
            sigma.append(float(self.table.item(row, 3).text()))

        # Запрос количества мест
        mest = int(self.seatsInput.text())

        # Вызов функций расчёта
        calculated_prices_lw, protected_seats_lw = calculate_littlewood(prices, mean, sigma, mest)
        calculated_prices_em, protected_seats_a, protected_seats_b = calculate_emsr(prices, mean, sigma, mest)

        # Обновление данных в output_window
        self.outputWindow.updateResults(calculated_prices_lw, protected_seats_lw, calculated_prices_em, protected_seats_a, protected_seats_b)
