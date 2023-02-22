a = input('курс рубля к доллару: ')
b = input('курс доллара к евро: ')
symbol = a.find('д')
symbol1 = a.find('=')
c = a[symbol1+2:symbol-1:]
symbol2 = b.find('е')
symbol3 = b.find('=')
d = b[symbol3+2:symbol2-1:]

print(1/float(c)/float(d))