import unittest
from tax import SimpleTaxCalculator


class TestIncomeTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        expected_tax = 10200
        actual_tax = self.calc.income_tax(60000)
        self.assertEqual(actual_tax, expected_tax)

    def test_income_equal_threshold(self):
        expected_tax = 14539.76
        actual_tax = self.calc.income_tax(85528)
        self.assertEqual(actual_tax, expected_tax)

    def test_income_above_threshold(self):
        expected_tax = 19170.8
        actual_tax = self.calc.income_tax(100000)
        self.assertEqual(actual_tax, expected_tax)


class TestVatTax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()
    
    def test_vat_tax_with_zero_price(self):
        actual = self.calc.vat_tax(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_vat_tax_with_max_float_price(self):
        actual = self.calc.vat_tax(float("inf"))
        expected = float("inf")
        self.assertEqual(actual, expected)

    def test_vat_tax_with_string_input(self):
        with self.assertRaises(TypeError):
            self.calc.vat_tax("10")


if __name__ == "__main__":
    unittest.main()
