import unittest
from solution import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [0])
        self.assertEqual(fibonacci(1), [0, 1])
        self.assertEqual(fibonacci(2), [0, 1, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1, 2])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8, 13])
