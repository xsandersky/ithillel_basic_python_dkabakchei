from random import randint

n = randint(1, 10)
x = int(input('Введи число от 1 до 10: '))


if x == n:
    print('Uгадал')
else:
    while x != n:
        if x > n:
            print('Твое число больше рандомного')
        else:
           print('Твое число меньше рандомного')
        x = int(input())
        
print('Угадал')