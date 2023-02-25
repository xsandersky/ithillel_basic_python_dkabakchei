from random import randint\


def diff_odd_even(num_limit, lower_bound, upper_bound): # returns int
    
    lst = []
    sum_even = 0
    sum_odd = 0

    for _ in range(num_limit):
        lst.append(randint(lower_bound, upper_bound))

    for num in lst:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even - sum_odd


def main():
    
    start_range = 0
    finish_range = 100
    n = randint(start_range, finish_range)
        
    print(diff_odd_even(n, start_range, finish_range))


main()