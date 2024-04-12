
from scipy.stats import norm
import numpy as np


def calculate_littlewood(prices, mean, stand, mest):
    # Сортировка данных
    sorted_data = sorted(zip(prices, mean, stand), key=lambda x: x[0])
    prices, mean, stand = zip(*sorted_data)  # Распаковка отсортированных значений

    protect = []  # Список для хранения защищенных мест
    for price in prices:
        rez = []  # Список для хранения результатов внутренних вычислений
        for higher_price, higher_mean, higher_stand in zip(prices, mean, stand):
            if higher_price > price:  # Сравнение только с более высокими ценами
                for x in np.arange(0, 1000, 0.1):
                    probability = norm.cdf(x, higher_mean, higher_stand)
                    survivor = 1 - probability
                    esmr = higher_price * survivor
                    if esmr <= price:
                        rez.append(x)
                        break
        if rez:  # Если список rez не пуст, суммируем его и добавляем в protect
            protect.append(sum(rez))
        else:
            protect.append(0)  # Если не найдено ни одного соответствия, добавляем 0

    # Расчет защищенных мест
    protected_seats = []
    for i in range(len(prices)):
        if i < len(protect):
            protected_seats.append(mest - protect[i])
        else:
            protected_seats.append(mest)

    return prices, protected_seats
