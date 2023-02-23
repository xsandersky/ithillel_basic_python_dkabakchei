def copydeep(obj):

    if isinstance(obj, list):
        lst = []
        for i in range(len(obj)):

            if isinstance(obj[i], list):
                lst.append(copydeep(obj[i]))
            elif isinstance(obj[i], tuple):
                lst.append(copydeep(obj[i]))
            else:
                lst.append(obj[i])

    elif isinstance(obj, tuple):
        lst = ()
        for i in range(len(obj)):

            if isinstance(obj[i], list):
                lst.append(copydeep(obj[i]))
            elif isinstance(obj[i], tuple):
                lst.append(copydeep(obj[i]))
            else:
                lst.append(obj[i])
    else:
        lst = obj

    return lst


def main():

    lst1 = [['b', ['a']]]#['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    #lst1[3].append(0)
    lst1[0][1].append('c')
    print(lst1, lst2, sep='\n')


main()