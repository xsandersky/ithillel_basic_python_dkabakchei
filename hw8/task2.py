def copydeep(obj):
    lst = []
    for i in range(len(obj)):
        
        if isinstance(obj[i], list):
            lst.append(copydeep(obj[i]))
        elif isinstance(obj[i], tuple):
            lst.append(copydeep(obj[i]))
        else:
            lst.append(obj[i])

    return lst





def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    print(lst1, lst2)



main()

