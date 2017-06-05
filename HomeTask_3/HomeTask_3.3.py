#3. Написать функцию, которая выводит на экран n первых четных чисел.
#>>func(3):
#>>2, 4, 6






def func(a):
    ccount = 0
    start = 1
    llist = []
    while ccount < a:
        if start % 2 == 0:
            llist.append(start)
            ccount += 1
            start += 1
        else:
            start += 1
    return llist


print(func(3))