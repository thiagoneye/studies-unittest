import unittest
from rectangle import area


class TestArea(unittest.TestCase):
    def test_area_invalid_value_should_raise_value_error(self):
        test_cases = [(-4, 5), (4, -5), (10, 0)]

        for width, height in test_cases:
            with self.subTest(width=width, height=height):
                with self.assertRaises(ValueError):
                    area(width, height)


if __name__ == "__main__":
    unittest.main()
