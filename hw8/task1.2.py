from random import randint


def index(lst, elem):  # returns integer or None
    for i in range(len(lst)):
        if lst[i] != elem:
            continue
        else:
            return i


def main():
    x = randint(3, 10)
    elem = int(input())
    random_lst = []

    for i in range(x):
        random_lst.append(randint(0, 1000))

    print(index(random_lst, elem))


main()



