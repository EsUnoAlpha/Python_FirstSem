"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""

import json


task = ["oleg", 24, ["Belarus", "Russia"], (24, 1), ["Moscow", "Vladikavkaz", 'Krasnodar', "Rostov", "Nalchik"]]
s = ['name', 'age', 'countries', 'name', 'time', 'cities']


object = {}
for i in range(2):
    object[s[i]] = task[i]

object[s[2]] = {}

k = 0
for i in range(3, 6):
    object[s[2]][s[i]] = task[i - 1]



print(object)
encoded = json.dumps(object, indent=4)

with open('Alex_Pykhtin_Task4.json', 'w+') as f:
    f.write(encoded)