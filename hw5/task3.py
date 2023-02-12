from math import pi

def cone_square_and_volume(radius, height):
    l = (height**2 + radius**2)**0.5 + height + radius  #сторона конуса
    s_line = pi * radius * l
    s_circle = pi * radius**2
    s_full = s_line + s_circle
    v = (pi * radius**2 * height) / 3
    return s_full, v


h = float(input('Висота: '))
r = float(input('Радіус: '))
s, v = cone_square_and_volume(r, h)

print(f'Площа конусу = {s} \nОб\'єм конусу = {v}')