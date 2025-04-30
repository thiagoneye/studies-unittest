"""
Using the unittest framework, create a TestSplitMethod class that inherits from the unittest.TestCase class and implements the following three tests:

- test_split_by_default()
    - test that checks if the code 'Python Testing'.split() returns a list ['Python', 'Testing']

- test_split_by_comma()
    - test that checks if the code 'open,high,low,close'.split(',') returns a list ['open', 'high', 'low', 'close']

- test_split_by_hash()
    - test that checks if the code 'summer#time#vibes'.split('#') returns a list ['summer', 'time', 'vibes']

You only need to define the class and the appropriate tests.

During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.
"""

import unittest

class TestSplitMethod(unittest.TestCase):
    def test_split_by_default(self):
        actual = 'Python Testing'.split()
        expected = ['Python', 'Testing']
        self.assertEqual(actual, expected)

    def test_split_by_comma(self):
        actual = 'open,high,low,close'.split(',')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(actual, expected)

    def test_split_by_hash(self):
        actual = 'summer#time#vibes'.split('#')
        expected = ['summer', 'time', 'vibes']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
