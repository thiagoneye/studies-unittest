import unittest


def string_lengths(strings):
    return list(map(len, strings))


class TestStringLengths(unittest.TestCase):
    def test_string_lengths(self):
        test_cases = [
            (["hello", "world"], [5, 5]),
            (["python", "is", "awesome"], [6, 2, 7]),
            ([], []),
            (["1", "22", "333", "4444"], [1, 2, 3, 4]),
        ]

        for actual, expected in test_cases:
            with self.subTest(actual=actual, expected=expected):
                self.assertEqual(string_lengths(actual), expected)


if __name__ == "__main__":
    unittest.main()
