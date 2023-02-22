list = []
while True:
    game = input()
    if game != '0':
        if game not in list:
            list.append (game)
            print('Игра добавлена')
        else:
            print('Игра уже существует')
    else:
        print('Спасибо')
        break
list.sort()
print (list)
