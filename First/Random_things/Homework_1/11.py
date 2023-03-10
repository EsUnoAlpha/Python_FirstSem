number = input('Введите номер')
if '+7' in number[0:2]:
    link = '<a href="tel:' + number + '">' +number + '</a>'
elif '8' in number [0: 1]:
    number = number.replace ('8', '+7', 1)
    link = '<a href="tel:' + number + '">' + number + '</a>'
else:
    number = '+7' + number
    link = '<a href="tel:' + number + '">' + number + '</a>'
print (link)