import unittest


def get_average_grade(grades):
    if not isinstance(grades, dict):
        raise TypeError("Input must be a dictionary")
    if not all(isinstance(key, str) for key in grades.keys()):
        raise TypeError("Keys must be strings")
    if not all(isinstance(value, (int, float)) for value in grades.values()):
        raise TypeError("Values must be numbers")
    if not grades:
        raise ValueError("Dictionary cannot be empty")
    return sum(grades.values()) / len(grades)


class TestGetAverageGrade(unittest.TestCase):
    def test_empty_dict(self):
        with self.assertRaises(ValueError):
            get_average_grade(dict())

    def test_non_string_keys(self):
        with self.assertRaises(TypeError):
            get_average_grade({"Gauss": 9.9, "Fermat": 9.5, ["Newton", "Einstein"]: 10.0})
        with self.assertRaises(TypeError):
            get_average_grade({"Gauss": 9.9, 38: 9.5, "Einstein": 10.0})

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            get_average_grade({"Gauss": [1000], "Fermat": 9.5, "Newton": 10.0})
        with self.assertRaises(TypeError):
            get_average_grade({"Gauss": 9.9, "Euler": "100", "Einstein": 10.0})


if __name__ == "__main__":
    unittest.main()
