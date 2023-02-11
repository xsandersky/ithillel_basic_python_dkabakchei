from math import cos, pi


def degrees2radians(x):
    u1 = (x * pi) / 180
    return u1


a, b, c = 60, 45, 40
x1, x2, x3 = cos(degrees2radians(a)), cos(degrees2radians(b)), cos(degrees2radians(c))

print(f'Косинус кута 60 градусів = {x1} \nКосинус кута 45 градусів = {x2} \nКосинус кута 40 градусів = {x3}')