#4. Написать функцию принимающую имя фигуры (квадрат, треугольник, ромб), ее размерность и рисует эту фигуру на экран
#Пример:
#>> print_figure(‘треугольник’, 3)
#*
#**
#***

def print_figure(f, n):

    def triangel(a):
        for i in range(a):
            print('*' * (i + 1))

    def square(a):
        for sq in range(a):
            print('*' * a)

    def rhombus(a):
        for rh in range(1, a + 1):
            print(' ' * (a - rh), end='')
            print('*' * rh, end='')
            print('*' * (rh - 1), end='')
            print()
        for rh1 in range(1, a + 1):
            print(' ' * rh1 , end='')
            print('*' * (a - rh1), end='')
            print('*' * ((a - rh1) -1), end='')
            print()
    if f == 'triangel':
        triangel(n)
    if f == 'square':
        square(n)
    if f == 'rhombus':
        rhombus(n)



print_figure('rhombus', 3)
