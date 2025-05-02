"""
Using the unittest framework create three classes named:

TestLstripMethod, TestStripMethod and TestRstripMethod that inherit from the unittest.TestCase class.

Then add two test methods to each class, testing the behavior of the methods appropriately:

- str.lstrip()
- str.strip()
- str.rstrip()

Choose appropriate names for the test cases and test methods at your discretion.
"""

import unittest

class TestLstripMethod(unittest.TestCase):
    def test_lstrip_with_space(self):
        self.assertEqual('  price,volume  '.lstrip(), 'price,volume  ')
 
    def test_lstrip_with_new_line_char(self):
        self.assertEqual('\nprice,volume\n'.lstrip(), 'price,volume\n')

class TestStripMethod(unittest.TestCase):
    def test_strip_with_space(self):
        self.assertEqual('  price,volume  '.strip(), 'price,volume')
 
    def test_strip_with_new_line_char(self):
        self.assertEqual('\nprice,volume\n'.strip(), 'price,volume') 

class TestRstripMethod(unittest.TestCase):
    def test_rstrip_with_space(self):
        self.assertEqual('  price,volume  '.rstrip(), '  price,volume')
 
    def test_rstrip_with_new_line_char(self):
        self.assertEqual('\nprice,volume\n'.rstrip(), '\nprice,volume')

if __name__ == "__main__":
    unittest.main()
