import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):
    def test_calc_tax(self):
        test_cases = [
            (60000, 0.2, 18, 5000),
            (60000, 0.2, 19, 12000),
            (60000, 0.2, 65, 12000),
            (60000, 0.2, 66, 8000),
        ]
        for amount, tax_rate, age, expected in test_cases:
            with self.subTest(
                amount=amount, tax_rate=tax_rate, age=age, expected=expected
            ):
                self.assertEqual(calc_tax(amount, tax_rate, age), expected)


if __name__ == "__main__":
    unittest.main()
