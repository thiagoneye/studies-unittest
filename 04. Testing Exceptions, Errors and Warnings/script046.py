import unittest
import warnings


def calculate_salary(wages, hours):
    if len(wages) != len(hours):
        raise ValueError("Wages and hours lists must have the same length")
    if not all(isinstance(wage, (int, float)) for wage in wages):
        raise TypeError("Wages list must contain numbers")
    if not all(isinstance(hour, (int, float)) for hour in hours):
        raise TypeError("Hours list must contain numbers")
    if not all(hour >= 0 for hour in hours):
        raise ValueError("Hours must be non-negative")
    if not all(wage >= 0 for wage in wages):
        raise ValueError("Wages must be non-negative")
    total_salary = sum([wages[i]*hours[i] for i in range(len(wages))])
    if total_salary == 0:
        warnings.warn("Total salary is zero or negative")
    return total_salary


class TestCalculateSalary(unittest.TestCase):
    def test_different_length_lists(self):
        with self.assertRaises(ValueError):
            calculate_salary([10, 15, 10, 20], [180, 185, 190, 170, 220])

    def test_non_numeric_wages(self):
        with self.assertRaises(TypeError):
            calculate_salary([10, 10, "15"], [180, 190, 180])

    def test_non_numeric_hours(self):
        with self.assertRaises(TypeError):
            calculate_salary([10, 10, 15], [180, 190, "180"])

    def test_negative_hours(self):
        with self.assertRaises(ValueError):
            calculate_salary([10, 10, 15], [180, -10, 180])

    def test_negative_wages(self):
        with self.assertRaises(ValueError):
            calculate_salary([10, -2, 15], [180, 190, 180])

    def test_zero_salary_warning(self):
        with self.assertWarns(UserWarning):
            calculate_salary([10, 10, 15], [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
