from time import sleep


class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

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


knight = Hero('Ричард', 50, 20, 25, 'Меч')
knight.print_info()
rascal = Hero('Хелен', 20, 5, 5, 'Лук')
rascal.print_info()
while True:
    if knight.health > 0:
        sleep(2)
        knight.strike_hero(rascal)
    else:
        sleep(2)
        print('Монстр победил!')
        break
    if rascal.health > 0:
        sleep(2)
        rascal.strike_enemy(knight)
    else:
        sleep(2)
        print('Рыцарь победил!')
        break
