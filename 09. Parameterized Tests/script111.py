import unittest


def reverse_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary")
    for key, value in input_dict.items():
        if not isinstance(value, int):
            raise ValueError("All values must be integers")
    return {value: key for key, value in input_dict.items()}


class TestReverseDict(unittest.TestCase):
    def test_reverse_dict(self):
        test_cases = [
            ({"one": 1, "two": 2, "three": 3}, {1: "one", 2: "two", 3: "three"}),
            ({"a": 0, "b": -1, "c": 10}, {0: "a", -1: "b", 10: "c"}),
            ({}, {}),
            ({"one": "1", "two": 2, "three": 3}, None),
            (["not a dictionary"], None),
            ({"one": 1, "two": "2", "three": 3}, None),
            ({"one": 1, "two": 2, "three": "3"}, None),
            ({"one": 1, "two": 2, 3: "three"}, None),
        ]

        for actual, expected in test_cases:
            with self.subTest(actual=actual, expected=expected):
                if not isinstance(actual, dict):
                    with self.assertRaises(TypeError):
                        reverse_dict(actual)
                elif not all(isinstance(value, int) for value in actual.values()):
                    with self.assertRaises(ValueError):
                        reverse_dict(actual)
                else:
                    self.assertEqual(reverse_dict(actual), expected)


if __name__ == "__main__":
    unittest.main()
