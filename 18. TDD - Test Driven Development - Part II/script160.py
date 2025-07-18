import unittest


def count_string(items):
    return sum(isinstance(item, str) for item in items)


class TestCountString(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.no_string = [1, 2]
        self.three_strings = ["c++", 3, "c", "java"]

    def test_count_string_empty_list(self):
        msg = "Correct the implementation of the count_string() function."
        self.assertEqual(count_string(self.empty_list), 0, msg)

    def test_count_string_without_string(self):
        msg = "Correct the implementation of the count_string() function."
        self.assertEqual(count_string(self.no_string), 0, msg)

    def test_count_string_with_three_string(self):
        msg = "Correct the implementation of the count_string() function."
        self.assertEqual(count_string(self.three_strings), 3, msg)


if __name__ == "__main__":
    unittest.main()
