class Point:
    '''The class of a point with x, y coordinates'''

    def __init__(self, x, y):
        '''Use the constructor to create a point with the coordinates x, y'''
        self.x = x
        self.y = y


class Circle:
    '''
    Circle Class. It implies creating a circle with x, y coordinates. 
    And checks if the third-party object Point is a part of our circle.
    '''

    def __init__(self, x, y):
        '''Using the constructor we create our point with x,y coordinates.'''
        self.x = x
        self.y = y
        self.r = 2


    def cheker_point(self, point):
         '''The cheker_point method checks if the third object (point) with x,y coordinates is part of our circle.'''
         return (point.x - self.x)**2 + (point.y - self.y)**2 <= self.r ** 2


if __name__=='__main__':
    point_1 = Point(2, 2)
    point_2 = Point(3,3)
    circle = Circle(4, 4)
    

    print(circle.cheker_point(point_1))
    print(circle.cheker_point(point_2))