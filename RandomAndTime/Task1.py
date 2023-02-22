"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""

from time import time
def chess():
    step = input('Введите ваш ход: ')
    start = time()
    alltime = 1800
    while step != 0:
        if step != 'off':
            end = time()
            total = round(end - start, 1)
            if total >= alltime:
                print('Время истекло')
                break
            else:
                left_time = (alltime - int(total))//60
                print(left_time)
                step = input('Введите ваш ход: ')
        else:
            print('Ходы окончены')
            break

chess()



