import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):
    def test_calc_tax_twenty_percent_and_eighteen_age(self):
        actual = calc_tax(60000, 0.2, 18)
        expected = 5000
        self.assertEqual(actual, expected)

    def test_calc_tax_twenty_percent_and_nineteen_age(self):
        actual = calc_tax(60000, 0.2, 19)
        expected = 12000
        self.assertEqual(actual, expected)

    def test_calc_tax_twenty_percent_and_sixty_five_age(self):
        actual = calc_tax(60000, 0.2, 65)
        expected = 12000
        self.assertEqual(actual, expected)

    def test_calc_tax_twenty_percent_and_sixty_six_age(self):
        actual = calc_tax(60000, 0.2, 66)
        expected = 8000
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
