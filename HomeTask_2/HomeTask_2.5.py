#3. Вывести таблицу умножения на экран.


a = int(input('enter number: '))
for i in range(1,11):
    print("{} * {} = {}".format(a, i, a * i))

