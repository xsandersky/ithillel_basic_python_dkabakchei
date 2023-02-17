def is_even(number): # returns boolean value
    return number % 2 == 0


def main():
    x = float(input())

    if is_even(x):
        print('Yes')
    else:
        print('No')


main()