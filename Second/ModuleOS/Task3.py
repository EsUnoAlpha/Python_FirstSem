"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""


import os

list = (os.listdir(r'C:\Users\16874\OneDrive\Рабочий стол\target'))

for i in list:
    if int(i) % 2 == 0:
        os.rename(fr'C:\Users\16874\OneDrive\Рабочий стол\target\{i}', fr'C:\Users\16874\OneDrive\Рабочий стол\target\LIGMA{i}')
