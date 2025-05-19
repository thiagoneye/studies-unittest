import unittest
from tax import calculate_tax


class TestCalculateTax(unittest.TestCase):
    def test_tax_with_eighteen_age(self):
        actual = calculate_tax(60000, 18)
        expected = 6000
        self.assertEqual(actual, expected)
    
    def test_tax_with_nineteen_age(self):
        actual = calculate_tax(60000, 19)
        expected = 10200
        self.assertEqual(actual, expected)

    def test_tax_with_sixty_five_age(self):
        actual = calculate_tax(60000, 65)
        expected = 10200
        self.assertEqual(actual, expected)
    
    def test_tax_with_sixty_six_age(self):
        actual = calculate_tax(60000, 66)
        expected = 9000
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
