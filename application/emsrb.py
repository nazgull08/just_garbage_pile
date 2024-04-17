from scipy.stats import norm
import numpy as np
import math

def calculate_emsr(names, prices, mean, sigma, mest):
    combined = list(zip(names, prices, mean, sigma))
    # Сортируем по цене (второй элемент в каждом кортеже)
    sorted_combined = sorted(combined, key=lambda x: x[1])
    # Разделяем отсортированный список кортежей обратно на четыре списка
    names_sorted, prices_sorted, mean_sorted, sigma_sorted = zip(*sorted_combined)

    names = list(names_sorted) 
    prices = list(prices_sorted) 
    mean = list(mean_sorted) 
    sigma = list(sigma_sorted) 
    #mean = [34, 39.6, 45.1, 17.3]
    #sigma = [11.3, 13.2, 15, 5.8]
    #names = ["d","c","b","a"]
    #prices2 = [520, 534, 567, 1050]
    #mean = [34, 39.6, 45.1, 17.3]
    #sigma = [11.3, 13.2, 15, 5.8]
    #names = ["d","c","b","a"]

    rez=[]
    protect=[]
    mylist=[]
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
        mylist.extend(rez)
        rez.clear()

    print(f"Rez ={rez}")
    print(f"List ={mylist}")
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

    # Обратный порядок списка names, чтобы соответствовать порядку в prices
    names.reverse()

    for y in range(len(prices)):
        if y != (len(prices) - 1):
            print(f"Для билетов ценовой категорией -- {round(prices[y], 3)}$ ({names[y]}) нужно предоставлять {mest - protect[y]} мест за данную сумму ")
        else:
            print(f"Для билетов ценовой категорией -- {round(prices[y], 3)}$ ({names[y]}) нужно предоставлять {mest} мест за данную сумму ")

    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    emsrb = []
    for price in prices:
        print(f"{price}$ ({names[prices.index(price)]})")
        if price < prices[len(summamoney)]:
            for x in np.arange(0, 1000, 0.1):
                probability = norm.cdf(x, mu[prices.index(price)], agsig[prices.index(price)])
                survivor = 1 - probability
                esmr = summamoney[prices.index(price)] * survivor
                if esmr < price:
                    emsrb.append((x, names[prices.index(price)]))
                    break
                elif esmr == price:
                    emsrb.append((x, names[prices.index(price)]))
                    break
    if emsrb:
        emsrb.append((protect[-1], names[-1]))  # добавляем последний защищенный элемент с его названием
    emsra = [(protect[i], names[i]) for i in range(len(protect))]

    demsra = {key: value for value, key in emsra}
    demsrb = {key: value for value, key in emsrb}
    for name in names:
        if name not in demsra:
            print("--a--a--")
            print(name)
            print(mest)
            demsra[name] = mest - sum(demsra.values())
        if name not in demsrb:
            print("--b--b--")
            print(name)
            print(mest)
            demsrb[name] = mest - sum(demsrb.values())

    print(f"ESMRB = {demsrb}")
    print(f"ESMRA = {demsra}")
    return demsra, demsrb
