a = input ()
b = a.split (' ')
for elem in b:
    if '@' in elem:
        print(elem)