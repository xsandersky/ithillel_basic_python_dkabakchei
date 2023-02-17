def fibonacci(n):
    x1 = 0
    x2 = 1
    for i in range(n-2):
        x_fibo = x1 + x2
        x1, x2 = x2, x_fibo
    return x_fibo


def main():
    n = 20
    print(f'20 число в последовательности Фибоначчи: {fibonacci(n)}')


main()