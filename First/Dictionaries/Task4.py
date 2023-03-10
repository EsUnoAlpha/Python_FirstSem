"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
dictionary  = {}
dictionary['key1'] = 'value1'
dictionary['key2'] = 'value2'
dictionary['key3'] = 'value3'
dictionary['key4'] = 'value4'
dictionary['key5'] = 'value5'
print (dictionary)
dictionary.update({'key1':'value5','key5':'value1'})
del dictionary['key2']
dictionary['new_key'] = 'new_value'
print (dictionary)