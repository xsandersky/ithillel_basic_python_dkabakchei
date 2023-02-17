def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    value_1 = (x1 - x2)**2 + (y1 - y2)**2 <= (r1 + r2)**2
    return value_1 <= (r1 + r2)**2 and value_1 + r1 >= r2


def main():
    x1, y1, r1 = float(input()), float(input()), float(input())
    x2, y2, r2 = float(input()), float(input()), float(input())

    if circles_intersect(x1, y1, r1, x2, y2, r2):
        print('Так, кола перетинаються')
    else:
        print('Ні, кола не перетинаються')


main()