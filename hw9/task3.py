def copydeep(obj):

    if isinstance(obj, (list, tuple)):
        value = []
        type_obj = type(obj)
        for val in obj:
            value.append(copydeep(val))
        value = type_obj(value)

    elif isinstance(obj, dict):
        value = {}
        for key in obj:
            value[key] = copydeep(obj[key])
    
    else:
        value = obj

    return value


def main():

    lst1 = ('a', 1, 2.0, ['b'])
    lst2 = copydeep(lst1)
    lst1[3].append(0)

    print(lst1, lst2, sep='\n')


main()