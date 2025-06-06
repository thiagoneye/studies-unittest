import unittest


def quotient(numbers):
    if numbers[1] == 0:
        raise ValueError("Division by zero")
    return numbers[0] / numbers[1]


class TestQuotient(unittest.TestCase):
    def test_quotient(self):
        test_cases = [
            ([1, 2], 0.5),
            ([10, 5], 2),
            ([2, 0], None),
            ([-10, 5], -2),
            ([0, 1], 0),
            ([0, 0], None),
        ]

        for actual, expected in test_cases:
            with self.subTest(actual=actual, expected=expected):
                if actual[1] == 0:
                    with self.assertRaises(ValueError):
                        quotient(actual)
                else:
                    self.assertEqual(quotient(actual), expected)


if __name__ == "__main__":
    unittest.main()
