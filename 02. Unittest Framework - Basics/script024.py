"""
Suppose you have the Rectangle class with the area() method.

Create the unit test class named TestRectangle and define the test cases:

- test_area_with_nonzero_dimensions()
- test_area_with_zero_dimensions()
- test_area_with_negative_width()
- test_area_with_negative_height()
- test_area_with_float_dimensions()
- test_area_with_large_dimensions()

In the test_area() method tests the area() method of the Rectangle class
by creating a new instance of the class with three different width and height values,
calling the area() method, and checking that the return value matches the expected
result using the assertEqual() method.
"""

import unittest

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._validate_params(width, height)
        self.width = width
        self.height = height

    def _validate_params(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")

    def area(self) -> float:
        return self.width * self.height

class TestRectangle(unittest.TestCase):
    def test_area_with_nonzero_dimensions(self):
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.area(), 2)

    def test_area_with_zero_dimensions(self):
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.area(), 0)

    def test_area_with_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-1, 1)

    def test_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, -1)

    def test_area_with_float_dimensions(self):
        rectangle = Rectangle(1.5, 2.5)
        self.assertEqual(rectangle.area(), 3.75)

    def test_area_with_large_dimensions(self):
        rectangle = Rectangle(1000000, 2000000)
        self.assertEqual(rectangle.area(), 2000000000000)

if __name__ == "__main__":
    unittest.main()
