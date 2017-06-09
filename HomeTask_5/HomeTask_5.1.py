#  1. Написать функцию, которая генерирует список списков (двух мерный массив) размерности NxN заполненный случайными числами от 100 до 999
# (использовать функцию random.randint(100, 999)
# пример
# >>gen_list(2)
# [[222, 113], [456, 500]]

from random import randint

def gen_list(a):
    lst = [[randint(100, 999) for _ in range(a)] for _ in range(a)]
    return print(lst)

gen_list(4)
