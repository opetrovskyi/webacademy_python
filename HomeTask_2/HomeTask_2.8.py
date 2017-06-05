#6. Доделать калькулятор. Спрашивать в цикле «продолжить?(y/n)».



while True:
    from math import sin,cos


    a, b, oper = float(input('Enter first number: \n')), \
                 float(input('Enter second number: \n')), \
                 input('Enter operation (+,-,/,*, **, sin, cos,): \n')

    if oper == '+':
        print(a + b)
    elif oper == '-':
        print(a - b)
    elif oper == '**':
        print(pow(int(a), int(b)))
    elif oper == '/':
        print(a / b)
    elif oper == '*':
        print(a * b)
    elif oper == 'sin':
        print("sin a = ", sin(a), 'sin b = ', sin(b) )
    elif oper == 'cos':
        print("cos a = ", cos(a), 'cos b = ', cos(b))
    else:
        print('invalid operator selected')

    exx = input('Wanna exit? yes/no ')
    if exx.lower() == 'yes':
        break