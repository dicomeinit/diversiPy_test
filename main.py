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

    @classmethod
    @abstractmethod
    def from_input_string(cls, input_string):
        raise NotImplementedError

    def __str__(self):
        return f'{self.name} Perimeter {self.perimeter} Area {self.area}'


class Square(Shape):
    def __init__(self, top_right_x, top_right_y, side):
        super().__init__('Square')
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.side = side

    @property
    def perimeter(self):
        return int(4 * self.side)

    @property
    def area(self):
        return int(self.side ** 2)

    @classmethod
    def from_input_string(cls, input_string):
        parts = input_string.split()
        if len(parts) != 6:
            raise ValueError
        top_right_x, top_right_y, side = map(int, (parts[2], parts[3], parts[5]))
        return cls(top_right_x, top_right_y, side)


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
        return int(2 * (length + width))

    @property
    def area(self):
        length = abs(self.top_right_x - self.bottom_left_x)
        width = abs(self.top_right_y - self.bottom_left_y)
        return int(length * width)

    @classmethod
    def from_input_string(cls, input_string):
        parts = input_string.split()
        if len(parts) != 7:
            raise ValueError
        top_right_x, top_right_y, bottom_left_x, bottom_left_y = map(int, (parts[2], parts[3], parts[5], parts[6]))
        return cls(top_right_x, top_right_y, bottom_left_x, bottom_left_y)


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__('Circle')
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    @property
    def perimeter(self):
        return int(2 * math.pi * self.radius)

    @property
    def area(self):
        return int(math.pi * (self.radius ** 2))

    @classmethod
    def from_input_string(cls, input_string):
        parts = input_string.split()
        if len(parts) != 6:
            raise ValueError
        center_x, center_y, radius = map(int, (parts[2], parts[3], parts[5]))
        return cls(center_x, center_y, radius)


class ShapeTests(unittest.TestCase):
    def test_str_square(self):
        square = Square(1, 1, 1)
        self.assertEqual(str(square), 'Square Perimeter 4 Area 1')

    def test_str_rectangle(self):
        rectangle = Rectangle(2, 2, 1, 1)
        self.assertEqual(str(rectangle), 'Rectangle Perimeter 4 Area 1')

    def test_str_circle(self):
        circle = Circle(1, 1, 2)
        self.assertEqual(str(circle), 'Circle Perimeter 12 Area 12')

    def test_parse_square(self):
        input_str = "Square TopRight 1 1 Side 1"
        square = Square.from_input_string(input_str)
        self.assertEqual(square.name, 'Square')
        self.assertEqual(square.perimeter, 4)
        self.assertEqual(square.area, 1)

    def test_parse_square_format(self):
        input_str = "Square"
        with self.assertRaises(ValueError):
            Square.from_input_string(input_str)

    def test_parse_square_format_not_all_params(self):
        input_str = "Square TopRight 1"
        with self.assertRaises(ValueError):
            Square.from_input_string(input_str)

    def test_parse_square_format_str_params(self):
        input_str = "Square TopRight 1 one Side 1"
        with self.assertRaises(ValueError):
            Square.from_input_string(input_str)

    def test_parse_rectangle(self):
        input_str = "Rectangle TopRight 2 2 BottomLeft 1 1"
        rectangle = Rectangle.from_input_string(input_str)
        self.assertEqual(rectangle.name, 'Rectangle')
        self.assertEqual(rectangle.perimeter, 4)
        self.assertEqual(rectangle.area, 1)

    def test_parse_circle(self):
        input_str = "Circle Center 1 1 Radius 2"
        circle = Circle.from_input_string(input_str)
        self.assertEqual(circle.name, 'Circle')
        self.assertEqual(int(circle.perimeter), int(2 * math.pi * 2))
        self.assertEqual(int(circle.area), int(math.pi * 2 ** 2))


if __name__ == "__main__":
    unittest.main()

