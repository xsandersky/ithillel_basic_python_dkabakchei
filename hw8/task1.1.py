def index(lst, elem):  # returns integer or None
    for i in range(len(lst)):
        if lst[i] != elem:
            continue
        else:
            return i


def main():
    random_lst = [2, 123, 22, 11234, 1, 44324 , 4, 523, 5, 6, 31]

    print(f'Индекс нашего числа 1 в списке random_lst = {index(random_lst, 1)}')
    print()
    print(f'В списке random_lst нет нашего элемента: {index(random_lst, 777)}')


main()
