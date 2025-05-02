"""
The following calculate_daily_return() function is given, which takes two arguments:
open and close (open and close price of a financial instrument from a trading session).

The function returns the value of the daily rate of return (in percent).

Complete the implementation of the TestCalculateDailyReturn class by adding three test methods:

- test_positive_return()
    using the method assertEqual check if code
    calculate_daily_return(349.0, 360.0) returns the daily rate of return 3.15

- test_negative_return()
    using the method assertEqual check if code
    calculate_daily_return(349.0, 340.0) returns the daily rate of return -2.58

- test_zero_return()
    using the method assertEqual check if code
    calculate_daily_return(349.0, 349.0) returns the daily rate of return 0.0

You only need to implement test methods. During the solution verification,
the tests are run and in case of any errors, the test report will be printed to the console.
"""

import unittest

def calculate_daily_return(open_price: float, close_price: float) -> float:
    return round(((close_price / open_price) - 1) * 100, 2)

class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self):
        actual = calculate_daily_return(349.0, 360.0)
        expected = 3.15
        self.assertEqual(actual, expected)

    def test_negative_return(self):
        actual = calculate_daily_return(349.0, 340.0)
        expected = -2.58
        self.assertEqual(actual, expected)

    def test_zero_return(self):
        actual = calculate_daily_return(349.0, 349.0)
        expected = 0.0
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
