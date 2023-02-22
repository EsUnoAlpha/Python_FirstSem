surname = input('Фамилия: ')
position = input('Должность: ')
amount = input('Кол-во человек в классе: ').split(',')
list =[]
list.append(surname)
list.append(position)
list.append(amount)
print(list)