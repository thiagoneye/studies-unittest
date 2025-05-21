import unittest
from tax import SimpleTaxCalculator


class TestCapitalGainsTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_capital_gains_tax_with_positive_profit(self):
        expected_tax = 190.0
        actual_tax = self.calc.capital_gains_tax(1000)
        self.assertEqual(actual_tax, expected_tax)

    def test_capital_gains_tax_with_zero_profit(self):
        expected_tax = 0.0
        actual_tax = self.calc.capital_gains_tax(0)
        self.assertEqual(actual_tax, expected_tax)

    def test_capital_gains_tax_with_negative_profit(self):
        expected_tax = 0.0
        actual_tax = self.calc.capital_gains_tax(-1000)
        self.assertEqual(actual_tax, expected_tax)

    def test_capital_gains_tax_with_large_profit(self):
        expected_tax = 190000.0
        actual_tax = self.calc.capital_gains_tax(1000000)
        self.assertEqual(actual_tax, expected_tax)

    def test_capital_gains_tax_with_float_profit(self):
        expected_tax = 9.5
        actual_tax = self.calc.capital_gains_tax(50.0)
        self.assertEqual(actual_tax, expected_tax)

    def test_capital_gains_tax_with_max_float_profit(self):
        expected_tax = float("inf")
        actual_tax = self.calc.capital_gains_tax(float("inf"))
        self.assertEqual(actual_tax, expected_tax)

    def test_capital_gains_tax_with_string_profit(self):
        with self.assertRaises(TypeError):
            self.calc.capital_gains_tax("profit")

    def test_capital_gains_tax_with_none_profit(self):
        with self.assertRaises(TypeError):
            self.calc.capital_gains_tax(None)


if __name__ == "__main__":
    unittest.main()
