#1.1
number_1 = input('Условие 1.1. Введи трехзначное число: ')
print(int(number_1[0]) + int(number_1[1]) + int(number_1[2]))


#1.2
number_2 = int(input('Условие 1.2. Введи трехзначное число: '))
num_1 = number_2 % 10
num_2 = number_2 // 10 % 10
num_3 = number_2 // 100
print(num_1 + num_2 + num_3)