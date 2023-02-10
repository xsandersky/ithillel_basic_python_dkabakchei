def triangle_square_and_perimeter(x, y):
    s = 0.5*a*b
    p = (a**2 + b**2)**0.5 + a + b
    return s, p



a = 3
b = 4
square, perimeter = triangle_square_and_perimeter(a, b)

print(f'Площа прямокутного трикутника = {square} \nПериметр прямокутного трикутника = {perimeter}')