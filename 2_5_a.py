# Task_5_a

prices = [57.8, 46.51, 97, 130, 23.8, 66.66, 45.5, 2.38, 40, 34.75, 238]
for price in prices:
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
