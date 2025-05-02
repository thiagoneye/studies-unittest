"""
Using the unittest framework create a TestUpper class that inherits
from the unittest.TestCase class and implements the following two tests:

- test_upper()
    test that checks if the code  'summer'.upper() returns string 'SUMMER'

- test_is_upper()
    test that checks if the code 'SUMMER'.isupper() returns the boolean value True
    test that checks if the code 'summer'.isupper() returns the boolean value False

You only need to define the class and the appropriate tests.

During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.
"""

import unittest

class TestUpper(unittest.TestCase):
    def test_upper(self):
        actual = 'summer'.upper()
        expected = 'SUMMER'
        self.assertEqual(actual, expected)

    def test_is_upper(self):
        self.assertTrue('SUMMER'.isupper())
        self.assertFalse('summer'.isupper())

if __name__ == '__main__':
    unittest.main()
