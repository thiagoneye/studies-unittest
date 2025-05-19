import unittest
import math


def circle_area(radius):
    """Calculate the area of a circle given its radius."""

    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('Radius must be positive.')

    return math.pi * radius ** 2


class TestCircleArea(unittest.TestCase):
    def test_area_with_radius_one(self):
        actual = circle_area(1)
        expected = 3.14159
        self.assertAlmostEqual(actual, expected, 5)

    def test_area_with_radius_three(self):
        actual = circle_area(3)
        expected = 28.27431
        self.assertAlmostEqual(actual, expected, 5)
    
    def test_incorrect_type(self):
        self.assertRaises(TypeError, circle_area, '4')
        self.assertRaises(TypeError, circle_area, None)
 
    def test_incorrect_value(self):
        self.assertRaises(ValueError, circle_area, 0)
        self.assertRaises(ValueError, circle_area, -3)


if __name__ == "__main__":
    unittest.main()
