import unittest
import math


def perimeter(radius):
    """The function returns the length of the circle."""

    if not isinstance(radius, (int, float)):
        raise TypeError('The radius must be of type int or float.')

    if radius <= 0:
        raise ValueError('The radius must be positive.')

    return 2 * math.pi * radius


class TestPerimeter(unittest.TestCase):
    def test_incorrect_type(self):
        self.assertRaises(TypeError, perimeter, "1")
    
    def test_incorrect_value(self):
        self.assertRaises(ValueError, perimeter, -1)
    
    def test_perimeter_with_radius_one(self):
        actual = perimeter(1)
        expected = 6.28318
        self.assertAlmostEqual(actual, expected, delta=0.00005)
    
    def test_perimeter_with_radius_two(self):
        actual = perimeter(2)
        expected = 12.56637
        self.assertAlmostEqual(actual, expected, delta=0.00005)


if __name__ == "__main__":
    unittest.main()
