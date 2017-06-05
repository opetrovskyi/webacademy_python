#4. Вывести на экран фигуры со звездочек (
#Треугольник, Квадрат, Ромб, Елочка, ступеньки
#)

def sepp():
    print('__' * 20)


a = 15

#triangle
for i in range(a):
    print('*' * (i + 1))

sepp()

#square
for sq in range(a):
    print('*' * a)

sepp()


#rhombus

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

sepp()
#fir-tree

for fir in range(2, a):
    for rh in range(1, fir + 1):
        print(' ' * (a - rh), end='')
        print('*' * rh, end='')
        print('*' * (rh - 1), end='')
        print()

sepp()

#stairs (if i got the task)
for sta in range(a):
    for _ in range(a):
        print('*' * a * sta)

sepp()
