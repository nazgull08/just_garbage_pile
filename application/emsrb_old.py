from scipy.stats import norm
import numpy as np
import math

def calculate_emsr(prices, mean, sigma, mest):
    sorted_data = sorted(zip(prices, mean, sigma), key=lambda x: x[0])
    prices, mean, sigma = zip(*sorted_data) if sorted_data else ([], [], [])

    # EMSR-a calculations: Protected seats
    protected_seats_a = []
    for index, price in enumerate(prices):
        rez = []
        for higher_index in range(index + 1, len(prices)):
            for x in np.arange(0, 1000, 0.1):
                probability = norm.cdf(x, mean[higher_index], sigma[higher_index])
                survivor = 1 - probability
                esmr = prices[higher_index] * survivor
                if esmr <= price:
                    rez.append(x)
                    break
        protected_seats_a.append(mest - (sum(rez) if rez else 0))

    # EMSR-b calculations: Expected revenue
    emsrb_revenue = []
    mu = [sum(mean[i+1:]) for i in range(len(mean) - 1)] + [0]
    for i in range(len(prices) - 1):
        num = sum(prices[j] * mean[j] for j in range(i+1, len(prices)))
        susig = sum(sigma[j] ** 2 for j in range(i+1, len(prices)))
        if mu[i] > 0:
            agsig = math.sqrt(susig)
            expected_revenue = num / mu[i]
            for x in np.arange(0, 1000, 0.1):
                probability = norm.cdf(x, mu[i], agsig)
                survivor = 1 - probability
                esmr = expected_revenue * survivor
                if esmr <= prices[i]:
                    emsrb_revenue.append(esmr)
                    break
        else:
            emsrb_revenue.append(0)

    # Ensure each array has the same length as prices for consistency
    if len(emsrb_revenue) < len(prices):
        emsrb_revenue.extend([0] * (len(prices) - len(emsrb_revenue)))

    return prices, protected_seats_a, emsrb_revenue
