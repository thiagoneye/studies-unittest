"""
Using the unittest framework create a TestLower class that inherits
from the unittest.TestCase class and implements the following two tests:

- test_lower()
    test that checks if the code 'Joe.Smith@mail.com'.lower() returns string 'joe.smith@mail.com'

- test_is_lower()
    test that checks if the code 'joe.smith@mail.com'.islower() returns the boolean value True
    test that checks if the code 'Joe.Smith@mail.com'.islower() returns the boolean value False

You only need to define the class and the appropriate tests.

During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.
"""

import unittest

class TestLower(unittest.TestCase):
    def test_lower(self):
        actual = 'Joe.Smith@mail.com'.lower()
        expected = 'joe.smith@mail.com'
        self.assertEqual(actual, expected)

    def test_is_lower(self):
        self.assertTrue('joe.smith@mail.com'.islower())
        self.assertFalse('Joe.Smith@mail.com'.islower())

if __name__ == '__main__':
    unittest.main()
