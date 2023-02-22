"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""


import json

with open("character.json", "r") as f:
    data = json.load(f)


def info(name, planet):
    print(
        f"Имя персонажа - {name}. Планета {planet}. \nЭпизоды: ")
    for i in data["episode"]:
        print(f"- {i}")


name = data["name"]
planet = data["origin"]["name"]

info(name, planet)
