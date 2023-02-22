"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os


os.makedirs(r'C:\Users\16874\OneDrive\Рабочий стол\target')
os.chdir(r'C:\Users\16874\OneDrive\Рабочий стол\target')
for i in range(1, 11):
    os.mkdir(f'{i}')