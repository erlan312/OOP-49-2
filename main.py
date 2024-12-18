# import lessons.lesson4  as mymodule
# from lessons import lesson4 as mymodule

# import random
# import math
# from json import JSONDecodeError


# mymodule.greet('Kirtito')
# print(mymodule.TEST)

# Модуль, Пакеты и Библиотеки
# Встроенные модули и Библиотеки
# Вешние пакеты, модули и Библиотеки

from colorama import init, Fore, Style

init()

print(Fore.RED + "This text is red!")
print(Fore.GREEN + "This text is green!")

from requests import get, post, put, delete