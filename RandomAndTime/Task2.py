"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""

from random import randint

amount1 = int(input('Введите количество участников: '))
amount2 = int(input('Введите количество участников: '))
team_num1 = randint(1, amount1)
team_num2 = randint (1, amount2)
print(team_num1,  team_num2)