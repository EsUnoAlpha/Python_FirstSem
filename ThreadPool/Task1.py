"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

from queue import Queue
from threading import Thread
from time import sleep

import sys


x = 0
def dobavlenie(queue, x):
    if type(x) == str:
        queue.put(x)


def otchislenie(queue):
     while True:
         try:
             item = queue.get()
             print(f'Студент {item} отчислен')
         except:
             ...

queue = Queue()
for i in ('Петров', "Иванов"):
    queue.put(i)


while x != 'off':
    thread1 = Thread(target=dobavlenie, args={queue, x})
    thread1.start()
    thread1.join()

    thread2 = Thread(target=otchislenie, args={queue, }, daemon=True)
    thread2.start()

    sleep(1)
    x = input('введите фамилию студента: ')






