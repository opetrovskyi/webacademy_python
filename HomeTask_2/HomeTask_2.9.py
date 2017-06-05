#7. Доделать программу «угадай число».


# do not remember what should be done more

from random import randint

count = 0
guess = randint(1, 5)
while count <= 2:
    number = int(input('number: '))
    if number == guess:
        print('You won!')
        break
    elif number <  guess:
        print('Your number is less than secret ')
    elif number > guess:
        print('Your number is greater than secret')
    count += 1