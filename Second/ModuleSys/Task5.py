"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import sys

if len(sys.argv) < 2:
    print('Не указано имя файла')
    sys.exit()
filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    commands = f.readlines()

for cmd in commands:
    cmd = cmd.strip()
    if not cmd:
        continue
    try:
        exec(cmd)
    except Exception as e:
        print(f'Ошибка "{cmd}": {e}')
