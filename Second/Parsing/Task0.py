import requests
import lxml
from bs4 import BeautifulSoup
import time
import random

cookies = {
    'stest201': '0',
    'stest207': 'acc0',
    'stest209': 'ct2',
    'PHPSESSID': 'f252c45689965b404c56b0739a0ce976',
    'user_public_id': 'OIKhjinJfcd1MBhH%2BIkP1hw5243n8ddg7ZCnr80gQwHUhEL3sZySWH7OMzdSJD9o',
    '_gcl_au': '1.1.1332955271.1678790890',
    '_gid': 'GA1.2.203090512.1678790891',
    'tmr_lvid': '54882541ea0982e3c913d12b1cc3594a',
    'tmr_lvidTS': '1678790890834',
    '_ym_uid': '1678790891698072713',
    '_ym_d': '1678790891',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    'afUserId': '6a05c6cc-b326-4bd5-8b10-65f082f4abe2-p',
    'AF_SYNC': '1678790893310',
    'promo1000closed': 'true',
    'tp_city_id': '38733',
    '_userGUID': '0:lf84tp3c:9wvSnDkbmCviu093SGqrPrH_Z_oIJog_',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%209aa3a980fa615a8397ca%22}',
    'qrator_ssid': '1678793670.336.d4Dawit5Fv5bK6tI-jm3u97qs40ke4qe9k02iv27dmv447vbh',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    'qrator_jsr': '1678793715.932.a5nnhW1ceFfnP1dt-af9l2duvdrgu3s95kdob72nicvc02778-00',
    'qrator_jsid': '1678793715.932.a5nnhW1ceFfnP1dt-lc5r8el9vqjsm7812h1qk9lq15b2mcas',
    'authorizeTopperClosed': 'true',
    'visitedPagesNumber': '13',
    'tmr_detect': '1%7C1678793827159',
    '_ga_RD4H4CBNJ3': 'GS1.1.1678790890.1.1.1678793827.58.0.0',
    '_ga': 'GA1.1.1304202688.1678790891',
    'mindboxDeviceUUID': 'd3064d3f-ebce-47a3-b941-82cee53f8973',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d3064d3f-ebce-47a3-b941-82cee53f8973%22%7D',
    'pageviewTimer': '1637.6270000000002',
}

headers = {
    'authority': 'sochi.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'stest201=0; stest207=acc0; stest209=ct2; PHPSESSID=f252c45689965b404c56b0739a0ce976; user_public_id=OIKhjinJfcd1MBhH%2BIkP1hw5243n8ddg7ZCnr80gQwHUhEL3sZySWH7OMzdSJD9o; _gcl_au=1.1.1332955271.1678790890; _gid=GA1.2.203090512.1678790891; tmr_lvid=54882541ea0982e3c913d12b1cc3594a; tmr_lvidTS=1678790890834; _ym_uid=1678790891698072713; _ym_d=1678790891; _ym_isad=1; _ym_visorc=w; afUserId=6a05c6cc-b326-4bd5-8b10-65f082f4abe2-p; AF_SYNC=1678790893310; promo1000closed=true; tp_city_id=38733; _userGUID=0:lf84tp3c:9wvSnDkbmCviu093SGqrPrH_Z_oIJog_; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%209aa3a980fa615a8397ca%22}; qrator_ssid=1678793670.336.d4Dawit5Fv5bK6tI-jm3u97qs40ke4qe9k02iv27dmv447vbh; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; qrator_jsr=1678793715.932.a5nnhW1ceFfnP1dt-af9l2duvdrgu3s95kdob72nicvc02778-00; qrator_jsid=1678793715.932.a5nnhW1ceFfnP1dt-lc5r8el9vqjsm7812h1qk9lq15b2mcas; authorizeTopperClosed=true; visitedPagesNumber=13; tmr_detect=1%7C1678793827159; _ga_RD4H4CBNJ3=GS1.1.1678790890.1.1.1678793827.58.0.0; _ga=GA1.1.1304202688.1678790891; mindboxDeviceUUID=d3064d3f-ebce-47a3-b941-82cee53f8973; directCrm-session=%7B%22deviceGuid%22%3A%22d3064d3f-ebce-47a3-b941-82cee53f8973%22%7D; pageviewTimer=1637.6270000000002',
    'if-none-match': '"14442b-Q/+wlw6UJb0MgdBi279I+VAk3lY"',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

result = {}

for i in range(1, 11):
    # time.sleep(random.randint(1,5))
    # response = requests.get('https://sochi.technopark.ru/smartfony/', params={'p':str(i)}, cookies=cookies, headers=headers)
    # print(response)
    # with open ('page_1.html', 'w', encoding="UTF-8") as f:
    #     f.write(response.text)



    with open (f'page{i}.html', 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file.read(), "lxml")
        container = soup.find_all("div", "product-card-big__container")
        for i in container:
            name = i.find("div", "product-card-big__name").text[13: -11]
            price = i.find("div", "product-prices__price").text[5: -5]
            result[name] = price
        print(result)