"""
Suppose you have the function that reads the number of lines from a file.

This function opens the file with the given filename, reads all the lines,
and returns the number of lines in the file.

Define a class called TestCountLines that inherits from unittest.TestCase.

Then define two test methods:
    - test_count_lines_of_existing_file():
        The first test case checks that the count_lines() function returns the
        correct number of lines for an existing file named evaluate.py.
        It should have 21 lines.
    - test_count_lines_of_non_existing_file():
        The second test case checks that the count_lines() function raises a
        FileNotFoundError exception when given a non-existing file named non
        existing_script.py.
"""

import unittest

def count_lines(filename: str) -> int:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {filename} not found") from e

class TestCountLines(unittest.TestCase):
    def test_count_lines_of_existing_file(self):
        actual = count_lines("evaluate.py")
        expected = 21
        self.assertEqual(actual, expected)

    def test_count_lines_of_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            count_lines("existing_script.py")

if __name__ == "__main__":
    unittest.main()
