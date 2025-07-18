import unittest


def map_longest(words):
    return max(len(word) for word in words) if words else 0


class TestMapLongest(unittest.TestCase):
    def setUp(self):
        self.words1 = ["sql", "r", "python"]
        self.words2 = ["sql", "r"]
        self.words3 = []

    def test_map_longest_should_be_six(self):
        msg = "Correct the implementation of the map_longest() function."
        self.assertEqual(map_longest(self.words1), 6, msg)

    def test_map_longest_should_be_three(self):
        msg = "Correct the implementation of the map_longest() function."
        self.assertEqual(map_longest(self.words2), 3, msg)

    def test_map_longest_should_be_zero(self):
        msg = "Correct the implementation of the map_longest() function."
        self.assertEqual(map_longest(self.words3), 0, msg)


if __name__ == "__main__":
    unittest.main()
