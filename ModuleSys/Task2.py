"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""


import sys


user_input = sys.stdin.readline()
if 'sys.in' in user_input:
    print('Command added')