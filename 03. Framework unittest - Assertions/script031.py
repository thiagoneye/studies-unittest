"""
The Doc class is given.

Using the unittest framework create a TestDoc class that inherits from
the unittest.TestCase class that implements two test methods:

- test_equal()
    checks if doc1 == doc2 use the assertEqual() method for this purpose

- test_not_equal()
    checks if doc3 != doc1 use the assertNotEqual() method for this purpose
    checks if doc3 != doc2 use the assertNotEqual() method for this purpose

Where doc1, doc2, doc3 are instances of Doc class, respectively:

    doc1 = Doc('Online')
    doc2 = Doc('Nature')
    doc3 = Doc('Technology')

You only need to implement the class and the appropriate test methods.
During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.
"""

import unittest

class Doc:
    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"

    def __eq__(self, other) -> bool:
        return len(self.string) == len(other.string)

    def __ne__(self, other) -> bool:
        return len(self.string) != len(other.string)

class TestDoc(unittest.TestCase):
    def test_equal(self):
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        self.assertEqual(doc1, doc2)

    def test_not_equal(self):
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        doc3 = Doc('Technology')
        self.assertNotEqual(doc3, doc1)
        self.assertNotEqual(doc3, doc2)

if __name__ == "__main__":
    unittest.main()
