import unittest


def sort_numbers(nums):
    return sorted(nums)
    
    
class TestSortNumbers(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(sort_numbers([]), [])

    def test_sort_one_number(self):
        self.assertEqual(sort_numbers([1]), [1])

    def test_sort_two_numbers(self):
        self.assertEqual(sort_numbers([2, 1]), [1, 2])

    def test_sort_many_numbers(self):
        self.assertEqual(sort_numbers([3, 2, -1]), [-1, 2, 3])


if __name__ == "__main__":
    unittest.main()
