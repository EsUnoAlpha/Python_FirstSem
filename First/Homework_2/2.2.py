x = 3
start = input('Напишите game, чтобы начать игру: ')
while start == 'game' and x > 0:
    answer = str(input('Угадайте число: '))
    if answer == 'off':
        break
    elif answer == '5':
        print ('Вы выиграли билет на концерт!')
    else:
        x -= 1
        if x == 0:
            print('У вас кончились попытки')
            x = 3
        else:
            print ('Попроуйте еще')
