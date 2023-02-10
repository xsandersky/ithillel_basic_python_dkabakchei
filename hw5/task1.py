from math import pi

def rad(x, y, z):
    u1 = (x * pi) / 180
    u2 = (y * pi) / 180
    u3 = (z * pi) / 180
    return u1, u2, u3

a, b, c = 60, 45, 40
u1, u2, u3 = rad(a, b, c)

print(f'Кут 60 градусів = {u1} \nКут 45 градусів = {u2} \nКут 40 градусів = {u3}')
