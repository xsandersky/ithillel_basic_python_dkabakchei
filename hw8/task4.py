def gen_primes(lst = []):
    divide = 0 

    for i in range(1, 101):
        divide = 0
        for j in range(1, i+1):
            if i % j == 0:
                divide += 1
        if divide > 1 and divide < 3:
            lst.append(i)

    return lst


def main():
    print(gen_primes())


main()