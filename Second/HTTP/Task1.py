"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests

for i in range(2):
    r = requests.get('https://cataas.com/cat')
    print(r)
    with open(f'cat{i}.jpg', 'wb') as f:
        f.write(r.content)


for k in range(2, 4):
    r = requests.get('https://cataas.com//cat?filter=pixel')
    print(r)
    with open(f'cat{k}.jpg', 'wb') as f:
        f.write(r.content)


for g in range(4, 6):
    r = requests.get('https://cataas.com/cat/cat?type=original')
    print(r)
    with open(f'cat{g}.jpg', 'wb') as f:
        f.write(r.content)