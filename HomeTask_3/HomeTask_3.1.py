#1. Написать функцию is_prime(a), Которая принимает число и возвращает True или False в зависимости от того, простое это число или нет (см. https://ru.wikipedia.org/wiki/Простое_число)
#Пример:
#>>is_prime(3)
#>>True
#>>is_prime(4)
#>>False


def is_prime(a):
    for _ in range(2, a):
        if (a / _).is_integer():
            exxit = 'False'
#            print('at least a /', _, 'is int')
            break
        else:
            exxit = "True"
    return exxit

#a = int(input('Enter a: '))

print(is_prime(11))

