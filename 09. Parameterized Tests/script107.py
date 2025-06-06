import unittest


def sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 1)


class TestSumOddNumbers(unittest.TestCase):
    def test_sum_odd_numbers(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 9),
            ([10, 11, 12, 13, 14, 15], 39),
            ([2, 4, 6], 0),
            ([], 0),
            ([1, 3, 5, 7], 16),
        ]

        for actual, expected in test_cases:
            with self.subTest(actual=actual, expected=expected):
                self.assertEqual(sum_odd_numbers(actual), expected)


if __name__ == "__main__":
    unittest.main()
