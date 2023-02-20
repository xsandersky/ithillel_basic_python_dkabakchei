from random import randint


def index(lst, elem):  # returns integer or None
    for i in range(len(lst)):
        if lst[i] != elem:
            continue
        else:
            return i


def main():
    x = randint(3, 10)
    elem = int(input('Введи число: '))
    random_lst = []

    for i in range(x):
        random_lst.append(randint(0, 1000))

    print(f'Индекс нашего числа {elem} в списке {random_lst} = {index(random_lst, elem)}')


main()
