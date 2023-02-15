def year(x):
    return x % 4 == 0 and x % 100 != 0 or x % 400 == 0


def main():
    x = int(input())
    print(year(x))


main()