import unittest
from tax import income_tax


class TestIncomeTax(unittest.TestCase):
    def test_tax_below_threshold(self):
        actual = income_tax(60000)
        expected = 10200
        self.assertEqual(actual, expected)

    def test_tax_equal_threshold(self):
        actual = income_tax(85528)
        expected = 14539.76
        self.assertEqual(actual, expected)

    def test_tax_above_threshold(self):
        actual = income_tax(100000)
        expected = 19170.8
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
