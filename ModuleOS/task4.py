""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""


import os

os.mkdir(r'C:\Users\16874\OneDrive\Рабочий стол\task4')
os.chdir(r'C:\Users\16874\OneDrive\Рабочий стол\task4')
file = open('answer.txt', 'w')
file.write('Я выполнил задание')