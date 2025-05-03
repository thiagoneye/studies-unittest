"""
Suppose you have a function calculate_grade() that takes a
list of student scores and returns the average grade.

Your task is to write test case to ensure that this function works properly.

Write your test case using built-in unittest module.

Define a class called TestCalculateGrade that inherits from
unittest.TestCase and implement the following test method:

- test_valid_input() - this test case checks that calling calculate_grade()
    with valid input returns the expected output - you should use six
    assertion methods with different inputs.
"""

import unittest

def calculate_grade(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("Elements of list must be numbers")
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("Elements of list must be between 0 and 100")
    return sum(scores) / len(scores)

class TestCalculateGrade(unittest.TestCase):
    def test_valid_input(self):
        with self.assertRaises(TypeError):
            calculate_grade(10)
        
        with self.assertRaises(ValueError):
            calculate_grade([])

        with self.assertRaises(TypeError):
            calculate_grade([0, 10, 50, "100"])

        with self.assertRaises(ValueError):
            calculate_grade([0, 10, 100, 150])

        self.assertEqual(calculate_grade([0, 50, 100]), 50)
        self.assertEqual(calculate_grade([100]), 100)

if __name__ == "__main__":
    unittest.main()
