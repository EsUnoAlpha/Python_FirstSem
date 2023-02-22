"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""

count = 0
with open(input('Введите название исходного файла: '), 'r') as f, open (input('Введите название нового файла: '), 'w+') as g:
    for line in f.readlines():
        count +=1
        g.write(str(count) + ': ' + line)
print('Процесс выполнен!')