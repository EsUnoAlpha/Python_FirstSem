"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""

import multiprocessing
def chetnie_chisla():
    chetnie = 0
    for i in range(1, 1000001):
        if i % 2 == 0:
            chetnie += i
    print(chetnie)


def nechetnie_chisla():
    nechetnie = 0
    for n in range(1, 1000001):
        if n % 2 != 0:
            nechetnie += n
    print(nechetnie)

if __name__  == '__main__':
    p1 = multiprocessing.Process(target=chetnie_chisla())
    p2 = multiprocessing.Process(target=nechetnie_chisla())

    p1.start()
    p2.start()




