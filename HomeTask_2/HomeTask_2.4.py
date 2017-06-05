#2.1 Считать целое число с клавиатуры. Если число делится на 5 вывести на экран слово ‘fiz’,
# если число делится на 3 вывести ‘buz’, если число делится на 3 и 5 вывести ‘fizbuz’.


a = int(input('enter number: \n >>'))

print('fizbuz') if (a / 3 ).is_integer() and (a / 5 ).is_integer() else print('fiz') if (a / 5 ).is_integer() else\
    print('buz') if (a / 3 ).is_integer() else print()
