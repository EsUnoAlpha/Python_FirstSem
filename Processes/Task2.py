"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""


import multiprocessing

def square():
    length = int(input('Введите длину: '))
    height = int(input('Введите высоту: '))
    width = int(input('Введите ширину: '))

    square = ((length*height)*2) + ((width*height)*2)


    with open('craska.txt', 'w') as f:
        f.write('Площадь команты: ')
        f.write(str(square))

def raschet():
    with open ('craska.txt', 'a+') as f:
        f.seek(16)
        square = int(f.read())
        f.write('\nРасход: ')
        f.write(str(square * 5))



if __name__ == '__main__':
    p1 = multiprocessing.Process(target=square())
    p2 = multiprocessing.Process(target=raschet())

    p1.start()
    p1.join()

    p2.start()
    p2.join()