from scipy.stats import norm
import numpy as np
import math


price = 0
prices = []
sigma = []
mean = []

data = list(zip(prices, mean, sigma))
sorted_data = sorted(data, key=lambda x: x[0])

prices = [item[0] for item in sorted_data]
mean = [item[1] for item in sorted_data]
sigma = [item[2] for item in sorted_data]

mest = int(input("Число мест на рейсе: "))
"""""
prices = [125, 290, 420, 500]
mean = [0, 35.1, 44.2, 16.5]
sigma = [0, 11.2, 15, 5.6]
"""""
"""""
prices = [165, 320, 425, 500]
mean = [0, 35.1, 44.2, 16.5]
sigma = [0, 11.2, 15, 5.6]
"""""
"""""
prices = [200, 400, 600, 800, 1000, 1200]
mean = [36.3, 26.9, 19.9, 14.8, 10.9, 31.2]
sigma = [12.0, 10.4, 8.9, 7.7, 6.6, 11.2]
"""""

prices = [520, 699, 950, 1050]
mean = [34.0, 39.6, 45.1, 17.3]
sigma = [11.3, 13.2, 15, 5.8]

"""""
prices = [520, 534, 567, 1050]
mean = [34, 39.6, 45.1, 17.3]
sigma = [11.3, 13.2, 15, 5.8]
"""""
rez=[]
protect=[]
list=[]
test=0

print(f"////////////")
for price in prices:
    for y in range(len(prices)):
        if prices[y]>price:
            test+=1
            for x in np.arange(0,1000, 0.1):
                probability = norm.cdf(x, mean[y], sigma[y])
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

print(f"Rez ={rez}")
print(f"List ={list}")
print(f"Protect ={protect}")



for y in range(len(prices)):
    if y != (len(prices)-1):
        print(f"Для билетов ценовой категорией -- {round(prices[y], 3)}$ нужно предоставлять {mest-protect[y]} мест за данную сумму ")
    elif y == (len(prices)-1):
        print(f"Для билетов ценовой категорией -- {round(prices[y], 3)}$ нужно предоставлять {mest} мест за данную сумму ")

#Начало EMSR-b
num=0
scet=0
susig=0
mu=[]
print(f"//////////////")
print(f"{mean}")
for i in range(len(mean)-1):
    mu.append(sum(mean[i+1:]))
    #mu=[sum(mean),sum(mean[2:]), sum(mean[3:])]
summamoney=[]
agsig=[]
for j in range(len(prices)):
    if j > 0 and j != (len(prices)-1):
        for i in range(len(prices)):
            if i >= j:
                num += prices[i]*mean[i]
                print(f"Значение num = {prices[i]*mean[i]}, Значение цен{prices[i]}, значение спроса {mean[i]}")

                susig = susig + pow(sigma[i], 2)
        print(f"переход {j}")
        agsig.append(math.sqrt(susig))
        susig=0
        summamoney.append(num/mu[j-1])
        num=0

print(f"Значение весов{mu}")
print(f"Значение суммы{summamoney}")
print(f"Значение новой сигма{agsig}")

print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
emsrb = []
for price in prices:
    print(price)
    print(prices.index(price))
    if price < prices[len(summamoney)]:
        for x in np.arange(0, 1000, 0.1):
            probability = norm.cdf(x, mu[prices.index(price)], agsig[prices.index(price)])
            survivor = 1 - probability
            esmr = summamoney[prices.index(price)] * survivor
            if esmr < price:
                emsrb.append(x)
                break
            elif esmr == price:
                emsrb.append(x)
                break
if emsrb != []:
    emsrb.append(protect[-1])
emsra = protect
print(f"ESMRB = {emsrb}")
print(f"ESMRA = {emsra}")
