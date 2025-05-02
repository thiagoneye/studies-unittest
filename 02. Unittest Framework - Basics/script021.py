"""
Using the unittest framework create two classes named:

TestStartsWithMethod and TestEndsWithMethod that inherit from the unittest.TestCase class.

The TestStartsWithMethod class implements two test methods:

- test_startswith_one_letter()
    test that checks if the code 'unittest'.startswith('u') returns the boolean value True
    test that checks if the code 'unittest'.startswith('U') returns the boolean value False

- test_startswith_four_letters()
    test that checks if the code 'http://www.e-smartdata.org/'.startswith('http') returns the boolean value True
    test that checks if the code 'www.e-smartdata.org/'.startswith('http') returns the boolean value False

The TestEndsWithMethod class implements one test method:

- test_endswith_three_letter()
    test that checks if the code 'e-smartdata.org'.endswith('org') returns the boolean value True
    test that checks if the code 'e-smartdata.org'.endswith('com') returns the boolean value False

You only need to define classes and the appropriate test methods.
During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.
"""

import unittest

class TestStartsWithMethod(unittest.TestCase):
    def test_startswith_one_letter(self):
        self.assertTrue('unittest'.startswith('u'))
        self.assertFalse('unittest'.startswith('U'))
    
    def test_startswith_four_letters(self):
        self.assertTrue('http://www.e-smartdata.org/'.startswith('http'))
        self.assertFalse('www.e-smartdata.org/'.startswith('http'))
    
class TestEndsWithMethod(unittest.TestCase):
    def test_endswith_three_letter(self):
        self.assertTrue('e-smartdata.org'.endswith('org'))
        self.assertFalse('e-smartdata.org'.endswith('com'))

if __name__ == '__main__':
    unittest.main()

