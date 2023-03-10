"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
import json

import requests


characters = []


for i in range(13, 13*5 + 1):
    get = requests.get(f'https://rickandmortyapi.com/api/character/{i}')
    data = get.json()
    characters.append({
        'name': data['name'],
        'planet' : data['origin']['name'],
        'episode': data['episode']
    })
with open ('R%M.json', 'w') as f:
    json.dump(characters, f, indent=4)


print('Завершено!')

