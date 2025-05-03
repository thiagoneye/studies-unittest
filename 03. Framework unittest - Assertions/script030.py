"""
The Doc class is given.

Using the unittest framework create a TestDoc class that inherits from
the unittest.TestCase class that implements two test methods:

- test_less_than()
    checks if doc2 < doc1 - use the assertLess() method for this purpose
    checks if doc3 < doc1 - use the assertLess() method for this purpose

- test_greater_than()
    checks if doc1 > doc2 - use the assertGreater() method for this purpose
    checks if doc1 > doc3 - use the assertGreater() method for this purpose

Where doc1, doc2, doc3 are instances of Doc class, respectively:

    doc1 = Doc('Technology')
    doc2 = Doc('Online')
    doc3 = Doc('Nature')

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

    def __lt__(self, other) -> bool:
        return len(self.string) < len(other.string)

    def __gt__(self, other) -> bool:
        return len(self.string) > len(other.string)

class TestDoc(unittest.TestCase):
    def test_less_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertLess(doc2, doc1)
        self.assertLess(doc3, doc1)

    def test_greater_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertGreater(doc1, doc2)
        self.assertGreater(doc1, doc3)

if __name__ == "__main__":
    unittest.main()
