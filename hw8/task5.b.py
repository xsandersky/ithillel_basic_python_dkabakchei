from random import randint


def get_max_digit(number):
    maxi = 0
    while number != 0:
        if number % 10 > maxi:
            maxi = number % 10
        number = number // 10
    return maxi


def main():
    a = randint(100000000000, 999999999999)
    
    print(get_max_digit(a))


main()