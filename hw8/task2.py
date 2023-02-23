def copydeep(obj):

    if isinstance(obj, list):
        value = []
        for i in range(len(obj)):
            value.append(copydeep(obj[i]))

    elif isinstance(obj, tuple):
        value = ()
        for i in range(len(obj)):
            value += (copydeep(obj[i]),)

    else:
        value = obj

    return value


def main():

    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    lst1[3].append(0)

    print(lst1, lst2, sep='\n')


main()