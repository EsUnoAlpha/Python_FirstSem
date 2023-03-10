"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def index_counter(weight, height):
    index = weight / (height*height)
    return index

def IMT_counter():
    index1 = index_counter(weight, height)
    if index1 < 18.5:
        print('Недостаточный вес')
    elif index1 >= 18.5 and index1 <= 25:
        print ('ИМТ в норме')
    else:
        print ('Избыточный вес')

weight = float(input('Введите ваш вес: '))
height = float(input ('Введите ваш рост(в метрах): '))
IMT_counter ()