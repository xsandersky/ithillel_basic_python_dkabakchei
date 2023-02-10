def my_sum(*x, start = 0):
    y = start + sum(x)
    return y

x = my_sum(3,4,5,5,44, start=31)
print(f'Сумма чисел с заранее переданными аргументами в функцию = {x}, start изменили с 0 на 31 в функции')
print()

#2
a = []
for i in range(1, 4):
    i = a.append(int(input(f'Введи {i} число из 3: ')))
x1 = my_sum(*a)
x2 = my_sum(*a, start=15)
print(f'Сумма чисел из 3 введенных с клавиатуры чисел = {x1} start не тронут и = 0')
print(f'Сумма чисел из 3 введенных с клавиатуры чисел = {x2} start = 15')