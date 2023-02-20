def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = []

    for i in range(len(lst1)):
        if isinstance(lst1[i], (list, tuple)):
            lst2.append(list(lst1[i]))
        else:
            lst2.append(lst1[i])


    lst1[3].append(0)

    print(lst1[3], lst2[3])


main()
