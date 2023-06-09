"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""



from multiprocessing import Process, Pipe
from time import sleep
from random import randint

num = randint(1, 10)
time = 3


def subscription(time, conn):
    while time != 0:
        sleep(1)
        time -= 1
    print("Подписка закончилась")
    conn.send(True)
    conn.close()
    return


def game(num, conn):
    while True:
        if conn.poll():
            conn.close()
            return
        inp = int(input("Введите число: "))
        if inp == num:
            print(f"Вы угадали число")
            sleep(0.5)
            num2 = randint(1, 10)
            return game(num2, conn)
        else:
            print("Попробуйте ещё раз")
            sleep(0.5)


if __name__ == "__main__":
    first, second = Pipe()
    p1 = Process(target=subscription, args=(time, first), daemon=True)
    p1.start()
    game(num, second)