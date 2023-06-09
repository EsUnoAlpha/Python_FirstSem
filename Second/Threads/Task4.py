import os
import re
import threading
import time


def replace_ids(filepath):
    # Открываем файл для чтения и записи
    with open(filepath, 'r+') as file:
        contents = file.read()
        contents = re.sub(r'\bids\b', 'id', contents)
        file.seek(0)
        file.write(contents)
        file.truncate()


if __name__ == '__main__':
    start_time = time.time()
    filepaths = [os.path.join('Files', f) for f in os.listdir('Files')]

    # Создаем отдельный поток для каждого файла
    threads = []
    for filepath in filepaths:
        thread = threading.Thread(target=replace_ids, args=(filepath,))
        thread.start()
        threads.append(thread)

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f'Время выполнения программы: {end_time - start_time:.2f} секунд')
