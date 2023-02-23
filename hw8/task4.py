def gen_primes():

    lst = []

    for i in range(2, 101):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if flag == False:
            lst.append(i)
            
    return lst


def main():
    print(gen_primes())


main()