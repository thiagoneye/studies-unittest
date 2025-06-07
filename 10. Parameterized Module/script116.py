import unittest
from parameterized import parameterized


def sort_strings(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    for item in input_list:
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
    return sorted(input_list)


class TestSortStrings(unittest.TestCase):
    @parameterized.expand(
        [
            (["hello", "world"], ["hello", "world"]),
            (["z", "a", "c"], ["a", "c", "z"]),
            ([], []),
            (["hello", 123], None),
            ({"not": "a list"}, None),
            (["hello", None], None),
        ]
    )
    def test_sort_strings(self, input_list, expected_output):
        if expected_output is None:
            with self.assertRaises((TypeError, ValueError)):
                sort_strings(input_list)
        else:
            self.assertEqual(sort_strings(input_list), expected_output)


if __name__ == "__main__":
    unittest.main()
