"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
import json
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://class.sirius.ru/authorize')

search_login = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input')
# s_search.clear()
search_login.send_keys('')

search_pass = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input')
# s_search.clear()
search_pass.send_keys('')

search_pass.send_keys(Keys.ENTER)
time.sleep(1)
s_search = driver.find_element(By.XPATH, '/html/body/div[1]/div/header/div/div/div/nav/div/a[4]')
s_search.click()
time.sleep(1)

class_data = {}

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
days = soup.find_all('div', 'schedule__day')

for day in days:
    class_data[day.find("div", "column-40").text.strip()] = {}
    lessons = day.find_all("div", "columns")
    for j in range(1, len(lessons)):
        lesson = lessons[j]
        if lesson.find('span', 'schedule-lesson') is not None:
            if 'L1' in lesson.find('span', 'schedule-lesson').text.strip() or 'L2' in lesson.find('span',
                                                                                                  'schedule-lesson').text.strip():
                continue
            else:
                class_data[day.find("div", "column-40").text.strip()][
                    lesson.find('span', 'schedule-lesson').text.strip()] = lesson.find('div',
                                                                                       'schedule__day__content__lesson__room').text.strip()

with open('class.json', 'w', encoding="utf-8") as f:
    json.dump(class_data, f, indent=4, ensure_ascii=False)
