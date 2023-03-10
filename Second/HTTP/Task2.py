"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""

import requests

r = requests.get('https://randomuser.me/api')
d = r.json()
print('Hello, im', d['results'][0]['name']['first'], ', im from', d['results'][0]["location"]['country'], ', my phone number is', d['results'][0]['phone'])
