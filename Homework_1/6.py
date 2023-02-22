number = input ('Введите номер')
if '+7' in number[0:2]:
    code = (number [2:5:])
    print(code)
elif '8' in number[0:1]:
    code = (number [1:4:])
    print(code)
else:
    number = '+7' + number
    code = (number[2:5:])
    print (code)


