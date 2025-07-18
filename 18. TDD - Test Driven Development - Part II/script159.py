import unittest


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    def setUp(self):
        self.fact_0 = 1
        self.fact_1 = 1
        self.fact_2 = 2
        self.fact_3 = 6
        self.fact_6 = 720

    def test_factorial(self):
        msg = "Correct the implementation of factorial() function."
        self.assertEqual(factorial(0), self.fact_0, msg)
        self.assertEqual(factorial(1), self.fact_1, msg)
        self.assertEqual(factorial(2), self.fact_2, msg)
        self.assertEqual(factorial(3), self.fact_3, msg)
        self.assertEqual(factorial(6), self.fact_6, msg)


if __name__ == "__main__":
    unittest.main()
