import unittest
from rectangle import area, perimeter


class TestPerimeter(unittest.TestCase):
    def test_perimeter_incorrect_value_should_raise_value_error(self):
        test_cases = [(-40, 5), (4, -10), (0, 0)]

        for width, height in test_cases:
            with self.subTest(width=width, height=height):
                with self.assertRaises(ValueError):
                    perimeter(width, height)


if __name__ == "__main__":
    unittest.main()
