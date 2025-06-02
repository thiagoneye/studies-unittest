import unittest
from emp import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("John", "Smith", 40, 80000)

    def test_email(self):
        self.assertEqual(self.emp.email, "john.smith@mail.com")

    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Mike'
        self.assertEqual(self.emp.email, "mike.smith@mail.com")


if __name__ == "__main__":
    unittest.main()
