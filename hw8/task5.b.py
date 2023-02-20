from random import randint


def get_max_digit(number):
    maxi = 0
    while number != 0:
        if number % 10 > maxi:
            maxi = number % 10
        number = number // 10
    return maxi


def main():
    a = randint(pow(10, 12), pow(10, 13) - 1)
    
    print(get_max_digit(a))


main()