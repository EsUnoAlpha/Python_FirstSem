login = input('Придумайте логин: ')
forb_sym = '=?*^$№@_ '
count = 0
for i in login:
    if i in forb_sym:
        print('Недопустимый символ: ', i)
        break
    else:
        count += 1
    if count == len(login):
        print('Все хорошо!')
        break
