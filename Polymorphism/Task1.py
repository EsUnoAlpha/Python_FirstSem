"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""



class Man():
    def makesound(self):
        print('Имитирует кряканье')

    def clother(self):
        print('Человек в трико')


class Duck():
    def makesound(self):
        print('Крякает')

    def clother(self):
        print('Утка в тапках')


person = Man()
animal = Duck()

for smth in (person, animal):
    smth.makesound()
    smth.clother()


