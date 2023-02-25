from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    lst = []

    for _ in range(num_limit):
        lst.append(randint(lower_bound, upper_bound))
        
    lst.sort()
    value = lst[-1] - lst[0]

    return value


def main():

    start_range = 0
    finish_range = 100
    n = randint(start_range, finish_range)

    print(diff_min_max(n, start_range, finish_range))


main()