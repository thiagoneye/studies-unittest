"""
Suppose you have a function called calculate_average() that takes a
list of numbers as input and returns the average of those numbers.

Your task is to write test cases for this function using unittest.

Using the unittest framework create the unit test class named
TestCalculateAverage and implement the following test cases:

- test_calculate_average_valid_input() - 3 different assertions
- test_calculate_average_empty_input() - 1 assertion
- test_calculate_average_invalid_input() - 3 different assertions

Choose the input data for the tests according to the description of the test methods.
You should use a total of 7 assertion methods.
"""

import unittest

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_valid_input(self):
        self.assertEqual(calculate_average([1]), 1.0)
        self.assertEqual(calculate_average([-1, 2]), 0.5)
        self.assertEqual(calculate_average([0, 1, 2, 3, 4]), 2.0)

    def test_calculate_average_empty_input(self):
        actual = calculate_average([])
        expected = None
        self.assertEqual(actual, expected)

    def test_calculate_average_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_average("error")
        with self.assertRaises(TypeError):
            calculate_average([1, "2"])
        with self.assertRaises(TypeError):
            calculate_average([None, None, None])

if __name__ == "__main__":
    unittest.main()
