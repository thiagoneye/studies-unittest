import unittest
from rectangle import area


class TestArea(unittest.TestCase):
    def test_area(self):
        test_cases = [(1, 5, 5), (2, 10, 20), (100, 50, 5000)]

        for width, height, expected in test_cases:
            with self.subTest(width=width, height=height, expected=expected):
                self.assertEqual(area(width, height), expected)

    def test_area_incorrect_type_should_raise_type_error(self):
        test_cases = [(1, "5"), ("2", 10), ("two", "four")]

        for width, height in test_cases:
            with self.subTest(width=width, height=height):
                with self.assertRaises(TypeError):
                    area(width, height)


if __name__ == "__main__":
    unittest.main()
