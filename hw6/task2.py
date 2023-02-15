def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d**0.5) / 2*a
        x2 = (-b - d**0.5) / 2*a
        return x1, x2
    elif d == 0:
        x = -(b / (2*a))
        return x
    else:
        return None


def main():
    a, b, c, = float(input('Введи число a: ')), float(input('Введи число b: ')), float(input('Введи число c: '))
    print(solve_quadratic_equation(a, b, c))


main()