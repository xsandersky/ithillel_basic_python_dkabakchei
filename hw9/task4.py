def lchain(*iterables):  # returns list

    lst = []

    for value in iterables:
        lst.extend(value)

    return lst


def main():

    print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
    
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]


main()