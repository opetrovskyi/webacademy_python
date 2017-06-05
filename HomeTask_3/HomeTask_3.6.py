#5. Решить рекурсивно задачу нахождения n-го числа фиббоначи (см. https://ru.wikipedia.org/wiki/Числа_Фибоначчи)
#Пример
#>>fib(4)
#>>3



#0, 1, 1, 2, 3, 5, 8, 13,


def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 1
    return (fib(a - 2) + fib(a - 1))

print(fib(7))