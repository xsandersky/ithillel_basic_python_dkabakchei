class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 2


    def cheker_point(self, point):
         return (point.x - self.x)**2 + (point.y - self.y)**2 <= self.r ** 2


if __name__=='__main__':
    point = Point(2, 2)
    circle = Circle(4, 4)

    print(circle.cheker_point(point))