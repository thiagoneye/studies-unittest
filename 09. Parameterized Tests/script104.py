import unittest
from rectangle import area, perimeter


class TestPerimeter(unittest.TestCase):
    def test_perimeter(self):
        test_cases = [(1, 5, 12), (2, 10, 24), (100, 50, 300)]

        for width, height, expected in test_cases:
            with self.subTest(width=width, height=height, expected=expected):
                self.assertEqual(perimeter(width, height), expected)


if __name__ == "__main__":
    unittest.main()
