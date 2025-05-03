"""
The implementation of the Employee class is given.

Using the unittest framework create a TestEmployee class that inherits
from the unittest.TestCase class that implements two test methods:

- test_has_email_attr()
    checks whether the Employee class has the attribute email,
    if the attribute is missing, return the message:
        'The Employee class does not have an email attribute.'

- test_has_email_property()
    checks if the email attribute of the Employee class is of the type property.
    Use the assertIsInstance() method for this purpose.

You only need to implement the class and the appropriate test methods.

During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.
"""

import unittest

class Employee:
    """A simple class that describes an employee of the company."""

    TAX_RATE = 0.17
    BONUS_RATE = 0.10

    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self) -> str:
        return (f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com')

    @property
    def tax(self) -> float:
        return round(self.salary * self.TAX_RATE, 2)

    def apply_bonus(self) -> None:
        self.salary = int(self.salary * (1 + self.BONUS_RATE))

class TestEmployee(unittest.TestCase):
    def test_has_email_attr(self):
        msg = "The Employee class does not have an email attribute."
        self.assertTrue(hasattr(Employee, "email"), msg)

    def test_has_email_property(self):
        msg = "The Employee class email attribute is not a property."
        self.assertIsInstance(getattr(Employee, "email"), property, msg)

if __name__ == "__main__":
    unittest.main()
