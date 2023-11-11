import math
from abc import abstractmethod
import unittest


class Shape:
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, top_right_x, top_right_y, side):
        super().__init__('Square')
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.side = side

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, top_right_x, top_right_y, bottom_left_x, bottom_left_y):
        super().__init__('Rectangle')
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y

    @property
    def perimeter(self):
        length = abs(self.top_right_x - self.bottom_left_x)
        width = abs(self.top_right_y - self.bottom_left_y)
        return 2 ** (length + width)

    @property
    def area(self):
        length = abs(self.top_right_x - self.bottom_left_x)
        width = abs(self.top_right_y - self.bottom_left_y)
        return length * width


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__('Circle')
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)


class ShapeTests(unittest.TestCase):
    def test_square(self):
        square = Square(1, 1, 1)
        self.assertEqual(square.name, 'Square')
        self.assertEqual(square.perimeter, 4)
        self.assertEqual(square.area, 1)

    def test_rectangle(self):
        rectangle = Rectangle(2, 2, 1, 1)
        self.assertEqual(rectangle.name, 'Rectangle')
        self.assertEqual(rectangle.perimeter, 4)
        self.assertEqual(rectangle.area, 1)

    def test_circle(self):
        circle = Circle(1, 1, 2)
        self.assertEqual(circle.name, 'Circle')
        self.assertEqual(circle.perimeter, 2 * math.pi * 2)
        self.assertEqual(circle.area, math.pi * 2 ** 2)


if __name__ == "__main__":
    unittest.main()

