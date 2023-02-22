"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
from time import *
class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor


    def print_info(self):
        print('Поприветствуйте героя:', self.name)
        print('Уровень здоровья:', self.health)
        print('Броня:', self.armor)

class Magician(Hero):
    def hello(self):
        print('Верхом на коне появился бравый воин по имени', self.name)
        self.print_info()
        sleep(4)

    def attack(self, enemy):
        print('Удар! Храбрый воин', self.name, 'атакует', enemy.name, 'мечом!')
        enemy.armor -= 15
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print('Страшный удар обрушился на противника \nТеперь его броня:',
            (enemy.armor), ', а уровень здоровья', (enemy.health), '\n')
        sleep(5)

knight = Magician('Ричард', 50, 25, 20, 'меч')
knight.print_info()
rascal = Magician('Хелен', 20, 5, 5, 'лук')
rascal.print_info()
knight.hello()
rascal.hello()
knight.attack(rascal)