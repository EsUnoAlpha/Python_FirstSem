"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""


import csv

dict = {}
with open ('Task1.csv') as f:
    reader = csv.reader(f, delimiter = ';')
    for row in reader:
       dict[(row[0], row[1])] = {row[2], row[3]}

print(dict)
