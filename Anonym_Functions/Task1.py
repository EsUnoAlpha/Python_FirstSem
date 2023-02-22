x = input('Введите имя(off - выключить): ')
if x == 'off':
    print('Процесс завершен!')
else:
    y = (lambda x: x + ' ' + 'гений')
    print(y(x))
    while x != 'off':
        x = input('Введите имя(off - выключить): ')
        y = (lambda x: x + ' ' + 'гений')
        print(y(x))