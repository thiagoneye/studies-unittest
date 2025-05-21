import unittest
from tax import SimpleTaxCalculator


class TestIncomeTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_tax_below_threshold(self):
        expected_tax = 10200
        actual_tax = self.calc.income_tax(60000)
        self.assertEqual(actual_tax, expected_tax)

    def test_income_tax_equal_threshold(self):
        expected_tax = 14539.76
        actual_tax = self.calc.income_tax(85528)
        self.assertEqual(actual_tax, expected_tax)

    def test_income_tax_above_threshold(self):
        expected_tax = 19170.8
        actual_tax = self.calc.income_tax(100000)
        self.assertEqual(actual_tax, expected_tax)


if __name__ == "__main__":
    unittest.main()
