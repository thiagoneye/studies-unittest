import unittest
from rectangle import area, perimeter


class TestPerimeter(unittest.TestCase):
    def test_perimeter_invalid_type_should_raise_type_error(self):
        test_cases = [(4, "5"), ("2", 8), ("two", "three")]

        for width, height in test_cases:
            with self.subTest(width=width, height=height):
                with self.assertRaises(TypeError):
                    perimeter(width, height)


if __name__ == "__main__":
    unittest.main()
