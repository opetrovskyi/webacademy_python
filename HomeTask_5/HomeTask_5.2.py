# 2. Написать функцию, которая выводит двухмерный список в виде таблицы
# Пример
# >>print_list([[222, 113], [456, 500]])
# —————
# | 222 | 113 |
# —————
# | 456 | 500 |
# —————

from random import randint

def gen_list(a):
    lst = [[randint(100, 999) for _ in range(a)] for _ in range(a)]
    return lst

b=gen_list(3)
print(b)

def print_list(a):
    print("-" * len(a)* 4)
    for i in a:
        print(*i, end="\n", sep="|")
    print("-" * len(a) * 4)

print_list(b)