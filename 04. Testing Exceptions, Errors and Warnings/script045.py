import unittest


def calculate_grade(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("Elements of list must be numbers")
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("Elements of list must be between 0 and 100")
    return sum(scores) / len(scores)


class TestCalculateGrade(unittest.TestCase):
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            calculate_grade(10, 50, 100)

    def test_empty_list_input(self):
        with self.assertRaises(ValueError):
            calculate_grade([])

    def test_non_numeric_element(self):
        with self.assertRaises(TypeError):
            calculate_grade(["10", True, dict()])

    def test_out_of_range_element(self):
        with self.assertRaises(ValueError):
            calculate_grade([10, 100, 1000])


if __name__ == "__main__":
    unittest.main()
