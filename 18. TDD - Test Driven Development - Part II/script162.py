import unittest


def is_distinct(items):
    return len(items) == len(set(items))


class TestIsDistinct(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.numbers_with_duplicates = [3, 3, 1]
        self.numbers_without_duplicates = [3, 2, 1]
        self.strings_with_duplicates = ["c++", "c++", "r"]
        self.strings_without_duplicates = ["python", "java", "c"]

    def test_is_distinct_empty_list(self):
        msg = "Correct the implementation of the is_distinct() function."
        self.assertTrue(is_distinct(self.empty_list), msg)

    def test_is_distinct_with_numbers_should_return_false(self):
        msg = "Correct the implementation of the is_distinct() function."
        self.assertFalse(is_distinct(self.numbers_with_duplicates), msg)

    def test_is_distinct_with_numbers_should_return_true(self):
        msg = "Correct the implementation of the is_distinct() function."
        self.assertTrue(is_distinct(self.numbers_without_duplicates), msg)

    def test_is_distinct_with_strings_should_return_false(self):
        msg = "Correct the implementation of the is_distinct() function."
        self.assertFalse(is_distinct(self.strings_with_duplicates), msg)

    def test_is_distinct_with_strings_should_return_true(self):
        msg = "Correct the implementation of the is_distinct() function."
        self.assertTrue(is_distinct(self.strings_without_duplicates), msg)


if __name__ == "__main__":
    unittest.main()
