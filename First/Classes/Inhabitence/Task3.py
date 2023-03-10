"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""
class SpaceObject():
    def __init__(self, size):
        self.size = size

class Star(SpaceObject):
    def __init__(self, size, brightness):
        super().__init__(size)
        self.bright = brightness

    def shine(self):
        print('Звезда светит с яркостью', self.bright)

class Planet(SpaceObject):
    def __init__(self, size, population, growth):
        super().__init__(size)
        self.population = population
        self.growth = growth

    def population_years(self, years):
        print('Популяция планеты' ,self.population+(self.growth*years))

star = Star(44, 6)
star.shine()
planet = Planet(1000, 5400000, 2458)
planet.population_years(3)