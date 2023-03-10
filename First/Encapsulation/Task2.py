"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
from random import randint
from time import sleep


class Hero():
    def __init__(self, name, health, armor, power, weapon, rang):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.__rang = rang

    def print_info(self):
        sleep(1)
        print('Поприветствуйте героя:', self.name)
        sleep(1)
        print('Уровень здоровья:', self.health)
        sleep(1)
        print('Броня:', self.armor)
        sleep(1)
        print('Сила удара:', self.power)
        sleep(1)
        print('Оружие:', self.weapon, '\n')

    def getrang(self):
        return self.__rang

    def setrang(self, newrang):
        self.__rang = newrang

    def delrang(self):
        del self.__rang

    def strike_hero(self, rascal):
        print(
            'Удар! ' + self.name + ' атакует ' + rascal.name + ' с силой ' + str(self.power) + ', используя '
            + self.weapon + '\n'
        )
        rascal.armor -= self.power
        if rascal.armor < 0:
            rascal.health += rascal.armor
            rascal.armor = 0
        sleep(2)
        print(
            "Класс брони " + rascal.name + ' упал до ' + str(rascal.armor) + ', а количество здоровья уменьшилось до '
            + str(rascal.health) + '\n'
        )

    def strike_enemy(self, knight):
        print(
            'Удар! ' + self.name + ' атакует ' + knight.name + ' с силой ' + str(self.power) + ', используя '
            + self.weapon + '\n'
        )
        knight.armor -= self.power
        if knight.armor < 0:
            knight.health += knight.armor
            knight.armor = 0
        sleep(2)
        print(
            "Класс брони", knight.name, 'упал до ' + str(knight.armor) + ', а количество здоровья уменшьшилось до '
            + str(knight.health) + '\n'
        )


knight = Hero('Ричард', randint(100, 500), randint(20, 100), randint(5, 200), 'Меч', 'Герой')
knight.print_info()
rascal = Hero('Хелен', randint(100, 500), randint(20, 100), randint(5, 200), 'Лук', 'Монстр')
rascal.print_info()
while True:
    if knight.health > 0:
        sleep(2)
        knight.strike_hero(rascal)
    else:
        sleep(2)
        print('Монстр победил!')
        rascal.setrang('Победитель Арены')
        print(rascal.getrang())
        knight.delrang()
        break
    if rascal.health > 0:
        sleep(2)
        rascal.strike_enemy(knight)
    else:
        sleep(2)
        print('Рыцарь победил!')
        knight.setrang('Победитель Арены')
        print(knight.getrang())
        rascal.delrang()
        break



