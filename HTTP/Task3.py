"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
import json

import requests

with open('R&M.json', 'a') as f:
    for i in range(13, 13*5 + 1):
        get = requests.get(f'https://rickandmortyapi.com/api/character/{i}')
        jsonification = get.json()
        dickt = ({jsonification['name']: [jsonification['origin']['name'], jsonification['episode']]})
        json.dump(dickt, f)
        f.write(',\n')
    print('Завершено!')

