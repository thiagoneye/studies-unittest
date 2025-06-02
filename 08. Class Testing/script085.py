import unittest
from emp import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("John", "Smith", 40, 80000)

    def test_get_salary(self):
        self.assertEqual(self.emp.salary, 80000)

    def test_apply_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 88000)


if __name__ == "__main__":
    unittest.main()
