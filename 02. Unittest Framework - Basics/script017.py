"""
Using the unittest framework, the TestJoinMethod class was created.

The class has the following three tests:

- test_join_with_space()
    test that checks if the code ' '.join(['Python', '3.8']) returns a list 'Python 3.8'

- test_join_with_comma()
    test that checks if the code ','.join(['open', 'high', 'low', 'close']) returns a list 'open,high,low,close'

- test_join_with_new_line_char()
    test that checks if the code '\n'.join(['open', 'high', 'low', 'close']) returns a list 'open\nhigh\nlow\nclose'

First, run all tests (check the solution by clicking the 'Check solution' button).

Pay attention to the result. One of the tests was written incorrectly.

Try to correct it and run the tests again.
"""

import unittest

class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')

    def test_join_with_comma(self):
        actual = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'
        self.assertEqual(actual, expected)

    def test_join_with_new_line_char(self):
        actual = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
