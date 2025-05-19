import unittest


def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        actual = add_numbers(1, 2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_add_negative_numbers(self):
        actual = add_numbers(-1, -2)
        expected = -3
        self.assertEqual(actual, expected)

    def test_add_zero(self):
        actual = add_numbers(0, 0)
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
