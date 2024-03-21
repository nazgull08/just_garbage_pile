# Класс TicketClass представляет отдельный класс билетов, например, класс Y или E.
class TicketClass:
    # Конструктор класса инициализирует объект класса билетов с заданными именем и лимитом мест.
    def __init__(self, name, limit):
        self.name = name  # Название класса билетов, например "Y" или "E".
        self.limit = limit  # Общий лимит мест для данного класса.
        self.sold = 0  # Количество уже проданных билетов.

    # Метод для продажи билетов в данном классе.
    def sell_tickets(self, quantity):
        # Проверка, что продажа не превышает оставшееся количество билетов.
        if self.sold + quantity > self.limit:
            raise ValueError(f"Продажа невозможна: запрашивается {quantity} билетов, доступно только {self.limit - self.sold} в классе {self.name}.")
        self.sold += quantity  # Увеличение количества проданных билетов.

    # Метод для получения количества оставшихся билетов в данном классе.
    def remaining_tickets(self):
        return self.limit - self.sold  # Возвращает разницу между лимитом и проданными билетами.

# Класс TicketInventory управляет всеми классами билетов.
class TicketInventory:
    # Конструктор класса инициализирует пустую структуру для хранения классов билетов.
    def __init__(self):
        self.classes = {}  # Словарь для хранения объектов классов билетов.

    # Метод для добавления нового класса билетов с заданным лимитом.
    def add_class(self, name, limit):
        # Проверка на существование класса с таким же именем.
        if name in self.classes:
            raise ValueError(f"Класс {name} уже существует.")
        self.classes[name] = TicketClass(name, limit)  # Добавление нового класса.

    # Метод для продажи билетов в определенном классе.
    def sell_tickets(self, class_name, quantity):
        # Проверка на существование класса.
        if class_name not in self.classes:
            raise ValueError(f"Класс {class_name} не существует.")
        self.classes[class_name].sell_tickets(quantity)  # Продажа билетов в классе.

    # Метод для получения информации о количестве оставшихся билетов в классе.
    def get_remaining_tickets(self, class_name):
        # Проверка на существование класса.
        if class_name not in self.classes:
            raise ValueError(f"Класс {class_name} не существует.")
        return self.classes[class_name].remaining_tickets()  # Возврат количества оставшихся билетов.




inventory = TicketInventory()
inventory.add_class('Y', 150)
inventory.add_class('E', 10)

inventory.sell_tickets('Y', 10)
print(inventory.get_remaining_tickets('Y'))
