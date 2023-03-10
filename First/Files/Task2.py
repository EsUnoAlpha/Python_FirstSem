"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open ('test.txt', 'r') as f, open ('test2.txt','w+') as g, open('connector', 'w+') as h:
    g.write(', но у меня не получается.')
    g.seek(0)
    h.write(str(f.read()) + str(g.read()))
    h.seek(0)
    print(h.read())