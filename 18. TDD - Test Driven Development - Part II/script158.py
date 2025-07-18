import unittest


def filter_ge_four_char(words):
    return [word for word in words if len(word) >= 4]


class TestFilterGeFourChar(unittest.TestCase):
    def setUp(self):
        self.words1 = ["sql", "r", "java"]
        self.words2 = ["sql", "r", "python", "java"]
        self.words3 = []

    def test_filter_ge_four_char_with_one_item(self):
        msg = "Correct the implementation of the filter_ge_four_char() function."
        actual = filter_ge_four_char(self.words1)
        expected = ["java"]
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_with_two_item(self):
        msg = "Correct the implementation of the filter_ge_four_char() function."
        actual = filter_ge_four_char(self.words2)
        expected = ["python", "java"]
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_should_be_empty(self):
        msg = "Correct the implementation of the filter_ge_four_char() function."
        actual = filter_ge_four_char(self.words3)
        expected = []
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
