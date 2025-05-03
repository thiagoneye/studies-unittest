"""
Suppose you have the Calculator class with the divide method.

Create the unit test class named TestCalculator and define the following test cases:

- test_divide_positive_numbers()
- test_divide_zero_by_positive_number()
- test_divide_negative_by_positive_number()
- test_divide_by_zero_should_raise_error()

Use the setUp() and tearDown() methods to create an instance of the Calculator class
only once and delete it after the tests have been executed.
"""

import unittest

class Calculator:
    def divide(self, dividend: float, divisor: float) -> float:
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_divide_positive_numbers(self):
        actual = self.calculator.divide(4, 2)
        expected = 2.0
        self.assertEqual(actual, expected)

    def test_divide_zero_by_positive_number(self):
        actual = self.calculator.divide(0, 2)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_divide_negative_by_positive_number(self):
        actual = self.calculator.divide(-4, 2)
        expected = -2.0
        self.assertEqual(actual, expected)

    def test_divide_by_zero_should_raise_error(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(4, 0)

    def tearDown(self):
        del self.calculator

if __name__ == "__main__":
    unittest.main()
