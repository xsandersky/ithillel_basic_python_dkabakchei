from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    lst = []
    min_num = upper_bound
    max_num = lower_bound

    for _ in range(num_limit):
        lst.append(randint(lower_bound, upper_bound))
        
    for i in lst:
        if i < min_num:
            min_num = i

        if i > max_num:
            max_num = i

    return max_num - min_num


def main():

    start_range = 0
    finish_range = 100
    n = randint(start_range, finish_range)

    print(diff_min_max(n, start_range, finish_range))


main()