"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""


class BankAccount():
    def __init__(self,name, balance, pasport):
        self._name = name
        self.__balance = balance
        self.__pasport = pasport

    def getbalance(self):
        return self.__balance

    def getpasport(self):
        return self.__pasport

    def setpasport(self, newpasport):
        x = input('Введите пароль: ')
        if '12345' in x:
            print('Вызвали сеттер')
            self.__pasport = newpasport

    def setbalance(self, money):
        if self.__balance + money >= 0:
            self.__balance += money

    def deletepasport(self):
        y = input('Введите пароль: ')
        if '12345' in y:
            del self.__pasport

acc1 = BankAccount('Санек', 10000, 2123454)
print(acc1.getbalance())
print(acc1.getpasport())
acc1.setbalance(-5000)
acc1.setpasport(1112233)
print(acc1.getbalance())
print(acc1.getpasport())
acc1.deletepasport()
try:
    print(acc1.getpasport())
except:
    print('Паспортные данные были удалены.')





