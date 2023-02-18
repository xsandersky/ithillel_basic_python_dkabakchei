def sum_symbol_codes(first, last): # returns int
    sum = 0
    x1 = int(ord(first))
    x2 = int(ord(last))
    for i in range(x1, x2 + 1):
        sum += i
    return sum


def main():
    start_char, final_char = input(), input()
    print(sum_symbol_codes(start_char, final_char))


main()