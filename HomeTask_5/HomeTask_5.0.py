# # 0. Написать аналоги функций min и max
#


def min(*args):
    minn = args[0]
    for i in range(1, len(args)):
        if args[i] < minn:
            minn = args[i]
    return print(minn)

min(142, 1224, 3221, 123, 120, 322131)



def max(*args):
    maxnn = args[0]
    for i in range(1, len(args)):
        if args[i] > maxnn:
            maxnn = args[i]
    return print(maxnn)

max(142, 1224, 3221, 123, 120, 322131)