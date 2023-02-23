def get_max_digit(number):
    b = max(str(number))
    return int(b)


def main():
    numb = 190548031427

    print(get_max_digit(numb))


main()