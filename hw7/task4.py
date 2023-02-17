def sum_symbol_codes(first, last): # returns int
    sum = 0
    for i in range(first, last + 1):
        sum += i
    return sum


def main():
    start_char, final_char = int(ord(input())), int(ord(input()))
    print(sum_symbol_codes(start_char, final_char))


main()