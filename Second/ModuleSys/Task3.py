"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""

import sys

name = sys.argv[2]
text = sys.argv[1]

with open(name, "w+") as f:
    f.write(text)