def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2*a)
        x2 = None
        return x1, x2
    else:
        x1, x2 = None, None
        return x1, x2


def main():
    a, b, c, = float(input('Введи число a: ')), float(input('Введи число b: ')), float(input('Введи число c: '))
    x1, x2 = solve_quadratic_equation(a, b, c)

    if x1 is None and x2 is None:
        print('Корней нет')
    elif x2 is None:
        print(f'Корень уравнения = {x1:.2f}')
    else:
        print(f'У уравнения 2 корня: {x1:.2f} и {x2:.2f}')


main()