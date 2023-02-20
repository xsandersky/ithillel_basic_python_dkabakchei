def get_max_digit(number):
    b = max(str(number))
    return int(b)


def main():
    numb = 12233385

    print(get_max_digit(numb))


main()