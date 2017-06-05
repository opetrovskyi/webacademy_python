#2. Вывести на экран 10 первых простых чисел используют функцию задания 1
#Подсказка:
#>>if is_prime(num):
#      print(num)


def is_prime(a):
    if a == 1:
        return True
    for r in range(2, a):
        if a % r == 0:
            return False
    return True

ccount = 0
exxit = 0

while True:
    if exxit == 100:
        break
    if is_prime(ccount):
        print(ccount)
        ccount += 1
        exxit += 1
    else:
        ccount += 1
        

