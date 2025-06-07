import unittest
from parameterized import parameterized


def sum_even_numbers(numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))


class TestSumEvenNumbers(unittest.TestCase):
    @parameterized.expand(
        [
            ([1, 2, 3, 4, 5], 6),
            ([10, 20, 30, 40, 50], 150),
            ([1, 3, 5, 7, 9], 0),
            ([0, 2, 4, 6, 8], 20),
            ([], 0),
        ]
    )
    def test_sum_even_numbers(self, actual, expected_result):
        result = sum_even_numbers(actual)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
