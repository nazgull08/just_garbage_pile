
from scipy.stats import norm
import numpy as np

def calculate_littlewood(prices, mean, stand, mest):
    sorted_data = sorted(zip(prices, mean, stand), key=lambda x: x[0])
    prices = [item[0] for item in sorted_data]
    mean = [item[1] for item in sorted_data]
    stand = [item[2] for item in sorted_data]

    protect = []
    list = []
    rez = []
    for price in prices:
        for y in range(len(prices)):
            if prices[y] > price:
                for x in np.arange(0, 1000, 0.1):
                    probability = norm.cdf(x, mean[y], stand[y])
                    survivor = 1 - probability
                    esmr = prices[y] * survivor
                    if esmr < price:
                        rez.append(x)
                        break
                    elif esmr == price:
                        rez.append(x)
                        break

        if sum(rez) != 0:
            protect.append(sum(rez))
        list.extend(rez)
        rez.clear()

    protected_seats = []
    for y in range(len(prices)):
        if y != (len(prices)-1):
            protected_seats.append(mest - protect[y])
        else:
            protected_seats.append(mest)

    return prices, protected_seats

