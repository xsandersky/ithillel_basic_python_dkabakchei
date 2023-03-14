class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 1

    def cheker_point(self, point):
        if (point.x - self.x)**2 + (point.y - self.y)**2 <= self.r ** 2:
            return True
        else:
            return False



if __name__=='__main__':
    point = Point(2, 2)
    circle = Circle(3, 3)

    print(circle.cheker_point(point))