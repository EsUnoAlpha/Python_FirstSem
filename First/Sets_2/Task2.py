"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
test https://github.com/EsUnoAlpha/Lessons.gitList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
printSet = set()
list1 = []
for i in testList:
    if type(i) == set or type(i) == list or type(i) == dict:
        list1.append(i)
    else:
        printSet.add(i)
if len(testList) == len(printSet):
    print('True')
else:
    print('False' + '.', 'Изменяемые элементы: ', list1)



