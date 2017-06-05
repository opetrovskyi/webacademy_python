#2. Составить алгоритм увеличения всех трех, введённых с клавиатуры, переменных на 5,если среди них есть хотя бы две равные.
#  В противном случае выдать ответ «равных нет».

a, b, c = int(input('Enter first number: \n')), \
             int(input('Enter second number: \n')), \
             int(input('Enter third number: \n'))

if a == b or a == c or c == b:
    print(a + 5, b + 5, c + 5)
else:
    print('No equal numbers found')
