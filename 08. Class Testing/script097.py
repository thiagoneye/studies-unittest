import unittest
from bmi import BMI


class TestBMI(unittest.TestCase):
    def setUp(self):
        self.bmi = BMI(70, 1.8)

    def test_calculate_bmi(self):
        self.assertAlmostEqual(self.bmi.calculate_bmi(), 21.6, places=1)

    def test_is_healthy(self):
        self.assertEqual(self.bmi.is_healthy(), "healthy")

        self.bmi = BMI(45, 1.6)
        self.assertEqual(self.bmi.is_healthy(), "underweight")

        self.bmi = BMI(85, 1.8)
        self.assertEqual(self.bmi.is_healthy(), "overweight")

        self.bmi = BMI(110, 1.8)
        self.assertEqual(self.bmi.is_healthy(), "obese")


if __name__ == "__main__":
    unittest.main()
