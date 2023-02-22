"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def counter(nums):
    mid = round((sum(nums) / len(nums)), 1)
    bigger = []
    res = tuple()

    for i in range(len(nums)):
        if nums[i] > mid:
            bigger.append(nums[i])

    res = mid, bigger
    return res


print(counter([7, 8, 8, 4, 5, 6, 7, 8, 6, 5, 3, 5, 7, 6, 6, 9, 10]))

