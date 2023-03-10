cost1 = int(input())
cost2 = int(input())
cost3 = int(input())
if cost1 < cost2 and cost2 < cost3:
    cost = (cost1 + cost2+ cost3) / 2
    print (cost)
elif cost1 > cost2 and cost2 > cost3:
    cost = (cost1 + cost2 + cost3) / 3
    print (cost)
else:
    cost = (cost1 + cost2 + cost3)
    print (cost)
