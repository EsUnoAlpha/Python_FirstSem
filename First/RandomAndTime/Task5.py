"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""

from random import randint
from time import *
start = input('Start - запустить: ')
if 'start' in start:
    value1 = randint(1, 6)
    value2 = randint(1, 6)
    print('Подбрасываю кубики')
    sleep(2)
    print(value1, value2)
else:
    start = input('Введите "start')

