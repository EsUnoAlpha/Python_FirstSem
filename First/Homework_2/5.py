while True:
    x=int(input('Цена: '))
    if x!=0:
        y = int(input('Скидка: '))
        print(x-(x/100*y))
    else:
        break