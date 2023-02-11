def my_sum(*x, start=0):
    y = start + sum(x)
    return y

x = my_sum(3, 4, 5, 5, 44)
print(f'Сумма чисел с заранее переданными аргументами в функцию = {x}')
print()

#2
a = []
for i in range(1, 4):
    i = a.append(int(input(f'Введи {i} число из 3: ')))
x1 = my_sum(*a)
print(f'Сумма чисел из 3 введенных с клавиатуры чисел = {x1} start не тронут и = 0')