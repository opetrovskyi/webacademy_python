# Сгенерировать список размером 10х10 с помощью функции задания 1
# -Заменить по главной диагонали все числа на 0
# -Заменить все четные числа на 1, не четные на 0
# -Вывести строку таблицы с максимальной суммой элементов
# -Повернуть таблицу на 90 градусов, по часовой, против часовой    (Еще не сделал)

from random import randint

def gen_list(a):
    lst = [[randint(100, 999) for _ in range(a)] for _ in range(a)]
    return lst

b=gen_list(10)
c=gen_list(10)
d=gen_list(10)

def print_list(a):
    print("-" * len(a)* 4)
    for z in range(len(a)):
        a[z][z] = "{}".format('0' * 3)
    for i in a:
        print(*i, end="\n", sep="|")
    print("-" * len(a) * 4)

print_list(b)

def print_list_ch(a):
    print("-" * len(a)* 4)
    for z in a:
        for y in range(len(z)):
            if z[y] % 2 == 0:
                z[y] = 1
            else:
                z[y] = 0
    for i in a:
        print(*i, end="\n", sep="|")
    print("-" * len(a) * 4)

print_list_ch(c)

def print_list_sum(a):
    return print(max(a, key=sum))

print_list_sum(d)