# class Student():
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points
#         self.course = None
#
#     def output(self):
#         print(self.name, self.points, self.course)
#
#     def self_course(self, new_course):
#         self.course = new_course
#
# student = Student('Alex', 120)
# student.self_course('Programmer')
# student.output()



# class Rectangle():
#     def __init__(self, dlina, shirina):
#         self.dlina = dlina
#         self.shirina = shirina
#
#     def info(self):
#         print('Дан прямоугольник с длинной', self.dlina, 'и шириной', self.shirina)
#
#     def perimetr(self):
#         return 2*self.dlina + 2*self.shirina
#
#     def square(self):
#         return self.dlina * self.shirina
#
# rect  = Rectangle(4, 2)
# rect.info()
# print(rect.perimetr())
# print(rect.square())


# class Animal():
#     def __init__(self, vid_type, voice):
#         self.voice = voice
#         self.vid_type = vid_type
#
#     def print_t(self):
#         print(self.voice)
#
# cat = Animal('Кошка', 'Я ЗАХВАЧУ ПЛАНЕТУ')
# cat.print_t()
# print(cat.vid_type)
# dog = Animal('Собака','Я сожрал диван')
# dog.print_t()
# print(dog.vid_type)


class Bus():
    def __init__(self, speed, capacity, max_speed, empty_seats):
        self.speed = speed
        self.capacity = capacity
        self.max = max_speed
        self.empty = empty_seats

    def posadka(self, kolvo):
        if self.empty >= kolvo:
            self.empty -= kolvo
            print('Посадили - ', kolvo)
        else:
            print('Посадили -', self.empty)
            self.empty = 0
    def razgon(self, speed):
        if speed + self.speed < self.max:
            print(self.speed + speed)
            self.speed = speed
        else:
            print(self.max)
            self.speed = self.max

bus1=Bus(40, 80, 120, 10)
bus1.posadka(20)
bus1.razgon(70)

