"""Task 2"""


from time import *


prices = list()
for i in range(int(input('Введите количество поситителей: '))):
    age = int(input('Введите возраст посетителя: '))
    if age <= 2:
        prices.append(0)
    elif 3 <= age <= 12:
        prices.append(14.00)
    elif age >= 65:
        prices.append(18.00)
    else:
        prices.append(23.00)


sleep(1)
print('Идет подсчет цены...')
sleep(1)
print("%.2f" % sum(prices))
