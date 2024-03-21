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

    # Метод для расчета EMSR для каждого класса.
    def calculate_emsr(self, demand, prices):
        
        #Рассчитывает оптимальное количество билетов и цены для максимизации доходов.

        #:param demand: Словарь с ожидаемым спросом для каждого класса (например, {'Y': 100, 'E': 50}).
        #:param prices: Словарь с ценами билетов для каждого класса (например, {'Y': 200, 'E': 100}).
        
        # Перебираем все классы и рассчитываем EMSR для каждого.
        for class_name, class_obj in self.classes.items():
            # Получаем спрос и цену для текущего класса.
            class_demand = demand.get(class_name, 0)
            class_price = prices.get(class_name, 0)

            # Рассчитываем вероятность продажи каждого места (упрощенно).
            # Здесь мы принимаем вероятность как отношение спроса к общему количеству мест.
            # В реальных условиях вероятность может быть рассчитана сложнее.
            probability_of_sale = min(class_demand / class_obj.limit, 1.0)

            # Рассчитываем ожидаемый доход от продажи одного дополнительного места.
            emsr = class_price * probability_of_sale

            # Выводим информацию для каждого класса.
            print(f"Class {class_name}: EMSR is {emsr:.2f}")

    def apply_littlewoods_rule(self, demand, prices):
        
        #Применяет правило Littlewood для определения оптимального распределения мест между классами.

        #:param demand: Словарь с ожидаемым спросом для каждого класса.
        #:param prices: Словарь с ценами билетов для каждого класса.

        # Сортируем классы по цене в убывающем порядке.
        sorted_classes = sorted(self.classes.keys(), key=lambda x: prices[x], reverse=True)

        for i, class_name in enumerate(sorted_classes[:-1]):
            # Рассчитываем ожидаемый доход для текущего класса.
            current_class_revenue = prices[class_name] * min(demand[class_name] / self.classes[class_name].limit, 1.0)

            # Суммируем ожидаемые доходы для всех более дорогих классов.
            higher_classes_revenue = sum(
                prices[higher_class] * min(demand[higher_class] / self.classes[higher_class].limit, 1.0)
                for higher_class in sorted_classes[:i]
            )

            # Если ожидаемый доход от продажи последнего места в текущем классе меньше,
            # чем суммарный ожидаемый доход от более дорогих классов, 
            # остановить продажу в текущем классе.
            if current_class_revenue < higher_classes_revenue:
                print(f"Stop selling in class {class_name}: {current_class_revenue} vs. {higher_classes_revenue}")
            else:
                print(f"Continue selling in class {class_name}: {current_class_revenue} vs. {higher_classes_revenue}")


# Инициализация инвентаря билетов с различными классами.
inventory = TicketInventory()
inventory.add_class('Y', 150)  # Добавляем класс Y (эконом) с лимитом в 150 мест.
inventory.add_class('B', 50)   # Добавляем класс B (бизнес) с лимитом в 50 мест.
inventory.add_class('F', 20)   # Добавляем класс F (первый класс) с лимитом в 20 мест.

# Задаем ожидаемый спрос и цены для каждого класса.
demand = {'Y': 130, 'B': 45, 'F': 18}
prices = {'Y': 100, 'B': 250, 'F': 500}

# Вычисляем и выводим EMSR для каждого класса.
inventory.calculate_emsr(demand, prices)

# Применяем правило Литтлвуда и выводим решения о продажах.
inventory.apply_littlewoods_rule(demand, prices)

# Разбор того, что происходит:
# 1. EMSR (Expected Marginal Seat Revenue) рассчитывается для каждого класса. Это ожидаемый доход от продажи
#    одного дополнительного места, учитывая текущий спрос и цену. EMSR помогает понять, какой доход мы потенциально
#    теряем, продавая билеты в более дешевых классах, когда есть спрос на более дорогие.
#
# 2. Применение правила Литтлвуда позволяет определить, в какой момент стоит перестать продавать билеты в нижних
#    классах, чтобы оставить места для возможных продаж в более высоких классах, где цена билета выше.
#    Алгоритм перебирает классы от самых дорогих к более дешевым и сравнивает текущий возможный доход с доходом
#    от продажи в более дорогих классах. Если суммарный потенциальный доход от более дорогих классов превышает
#    текущий ожидаемый доход от более дешевого класса, продажи в этом классе стоит приостановить.
#
# На практике это означает, что если мы видим высокий спрос на более дорогие места, нам может быть выгоднее дождаться,
# пока эти места не будут проданы, вместо того чтобы продавать места в более дешевых классах.
