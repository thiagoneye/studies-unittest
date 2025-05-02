"""
Suppose you have a function called find_largest() that takes a
list of integers as input and returns the largest integer in the list.

Your task is to write test cases for this function using unittest.

Using the unittest framework create the unit test class named TestFindLargest
and implement the following test cases:

- test_find_largest_valid_input() - 3 different assertions
- test_find_largest_empty_input() - 1 assertion
- test_find_largest_invalid_input() - 3 different assertions

Choose the input data for the tests according to the description of the test methods.

You should use a total of 7 assertion methods.
"""

import unittest

def find_largest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers")
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

class TestFindLargest(unittest.TestCase):
    def test_find_largest_valid_input(self):
        self.assertEqual(find_largest([-3, -1, -2]), -1)
        self.assertEqual(find_largest([-1, 0, 4, 1, 2, 3]), 4)
        self.assertEqual(find_largest([2]), 2)

    def test_find_largest_empty_input(self):
        actual = find_largest([])
        expected = None
        self.assertEqual(actual, expected)

    def test_find_largest_invalid_input(self):
        with self.assertRaises(TypeError):
            find_largest(1)
        with self.assertRaises(TypeError):
            find_largest("error")
        with self.assertRaises(TypeError):
            find_largest([1, 2, 3, "4"])

if __name__ == "__main__":
    unittest.main()
