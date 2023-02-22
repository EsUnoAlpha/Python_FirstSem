"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""

count = input('Для выхода напишите "off" ')
dictionary = {}
while count !='off':
    start = input('Начать?')
    start.lower
    if start == 'yes':
        chart = input()
        singer = input()
        track = input()
    else:
        break
    dictionary[chart, singer] = track
    print (dictionary)
