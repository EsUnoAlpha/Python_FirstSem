import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor



queue = Queue()
number = int(input("Введите количество чисел: "))

def numbers(queue, number):
    for i in range(1, number + 1):
        num = random.randint(1, 1000)
        queue.put(num)


def devide(queue):
    while not queue.empty():
        num = queue.get()
        for i in range(1, num + 1):
            if num % i == 0:
                print(f"{i} - делитель числа {num}")


with ThreadPoolExecutor() as Th:
    Th.submit(numbers, queue, number)
    Th.submit(devide, queue)
    Th.submit(devide, queue)




