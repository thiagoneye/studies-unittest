"""
Suppose you have the StringReverser class with the reverse method.

Create the unit test class named TestStringReverser and define the test cases.

The test_reverse() method should test the reverse() method of the StringReverser class
by creating a new instance of the class, calling the reverse() method with different strings,
and checking that the return value matches the expected result using the assertEqual() method.

Test the reverse() method with three different strings:
- "hello"
- "12345"
- "" (empty string)

The expected results are "olleh", "54321", and "", respectively.
"""

import unittest

class StringReverser:
    def reverse(self, string):
        return string[::-1]

class TestStringReverser(unittest.TestCase):
    def test_reverse(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse("hello"), "olleh")
        self.assertEqual(reverser.reverse("12345"), "54321")
        self.assertEqual(reverser.reverse(""), "")

if __name__ == "__main__":
    unittest.main()
