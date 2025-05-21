import unittest
from emp import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        actual = Employee("John", "Smith", 40, 80000).email
        expected = "john.smith@mail.com"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
