from operator import add, sub, mul, truediv



oper = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}



def calc():
    while True:
        try:
            a,b = int(input('a=>: ')),int(input('b=>:'))
            input_operator = input('oper =>')
            result = oper[input_operator](a,b)
        except ZeroDivisionError:
            print('Cannot sub on 0')
        except ValueError:
            print('Values must be int, operation must be "+,-,*,/"')
        except:
            print('catch_all exception')
        else:
            return print(result)


calc()