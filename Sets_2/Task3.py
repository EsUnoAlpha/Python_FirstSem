"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)

newspaper_set = set(newspaper)
magazine_set = set(magazine)
both_set = set(both)
only_newspapers = newspaper_set - both_set
only_magazines = magazine_set - both_set
print(len(only_newspapers | only_magazines))
