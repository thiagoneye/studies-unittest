import unittest
from employees import Employee


class TestEmployee(unittest.TestCase):
    def test_employee_has_email_property(self):
        self.assertTrue(hasattr(Employee, "email"))
        self.assertIsInstance(Employee.email, property)


if __name__ == "__main__":
    unittest.main()
