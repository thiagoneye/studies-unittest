import unittest


def remove_duplicates(items):
    return list(set(items))


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.no_duplicates = [3, 3, 1]
        self.all_duplicates = ["c++", "c", "c"]

    def test_remove_duplicates_empty_list(self):
        msg = "Correct the implementation of the remove_duplicates() function."
        self.assertEqual(remove_duplicates(self.empty_list), [], msg)

    def test_remove_duplicates_without_string(self):
        msg = "Correct the implementation of the remove_duplicates() function."
        self.assertEqual(remove_duplicates(self.no_duplicates), [1, 3], msg)

    def test_remove_duplicates_with_three_string(self):
        msg = "Correct the implementation of the remove_duplicates() function."
        actual = sorted(remove_duplicates(self.all_duplicates))
        expected = ["c", "c++"]
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
