cost = int(input())
time = int(input())
if (time) >=10 and (time) <=12:
    cost1 = (cost)/2
    print (int(cost1))
elif (time) >=20 and (time) <=22:
    cost1 = (cost)/4
    print(int(cost1))
else:
    print(cost)
