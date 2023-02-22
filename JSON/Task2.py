"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""


import json

task = ["Alex", 24, ['Germany', 'Russia']]
s = ['name', 'age', 'countries']


def writer(task):
    object = {}
    for i in range(len(task)):
        object[s[i]] = task[i]
    encoded = json.dumps(object, indent=4)

    with open('Task2.json', 'w+') as f:
        f.write(encoded)


writer(task)
