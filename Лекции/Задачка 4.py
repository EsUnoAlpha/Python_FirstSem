category = input('Какая Категория вас интересует?: ')
cost = int(input ('Ценовая категория: '))
if category == 'продукты':
    if cost >=0 and cost <= 100:
        print ('Попробуйте нашу выпечку')
    elif cost >=100 and cost <=500:
        print('Как насчет орехов в шоколаде')
    else:
        print ('Попробуйте экзотические фрукты')
else:
    print ('Загляните в товары для дома')

