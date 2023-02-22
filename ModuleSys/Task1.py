"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""


import sys

list = []
for i in sys.argv:
    list.append(i)
if list[1] == '--name:':
    print('Hello', list[2])
else:
    print('Hello world')

