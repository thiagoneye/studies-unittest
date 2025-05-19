import unittest


def calculate_bmi(height, weight):
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive")
    bmi = weight / (height ** 2)
    return bmi


class TestCalculateBMI(unittest.TestCase):
    def test_calculate_bmi_normal(self):
        self.assertAlmostEqual(calculate_bmi(1.74, 70), 23.12, delta=0.005)

    def test_calculate_bmi_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(1.74, 0)

    def test_calculate_bmi_invalid_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-1, 70)


if __name__ == "__main__":
    unittest.main()
