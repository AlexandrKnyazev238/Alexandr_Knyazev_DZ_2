# Task_5_d

prices = [57.8, 46.51, 97, 130, 23.8, 66.66, 45.5, 2.38, 40, 34.75, 238]
print([f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп' for price in sorted(prices)[::-1][:5]])
