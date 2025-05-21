import unittest
from tax import SimpleTaxCalculator


def setUpModule():
    global calc
    calc = SimpleTaxCalculator()


class TestIncomeTax(unittest.TestCase):
    def test_income_below_threshold(self):
        self.assertEqual(calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(calc.income_tax(100000), 19170.8)


class TestVatTax(unittest.TestCase):
    def test_vat_tax_with_default(self):
        self.assertEqual(calc.vat_tax(100), 23.0)


class TestCapitalGainsTax(unittest.TestCase):
    def test_positive_profit(self):
        self.assertEqual(calc.capital_gains_tax(1000), 190.0)

    def test_zero_profit(self):
        self.assertEqual(calc.capital_gains_tax(0), 0.0)

    def test_negative_profit(self):
        self.assertEqual(calc.capital_gains_tax(-1000), 0.0)


if __name__ == "__main__":
    unittest.main()
