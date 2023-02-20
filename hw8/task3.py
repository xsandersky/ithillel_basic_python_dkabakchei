def main():
    lst1 = [5, '9', 0, '452', 6.5, '6', 1, 2]

    lst1_sort = sorted(lst1, key=float)
    print(f'# original list\n{lst1}\n# sorted list\n{lst1_sort}')

    print()
    print()

    lst2 = [472, 326, 1, '1101000', '99', 9, '20', 863, '0']

    lst2_sort = sorted(lst2, key=str)
    print(f'# original list\n{lst2}\n# sorted list\n{lst2_sort}')


main()