class Employee:
    """A class representing an employee of the company."""

    TAX_RATE = 0.17
    BONUS_RATE = 0.10

    def __init__(self, first_name, last_name, salary):
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    def __str__(self):
        return f'{self._first_name} {self._last_name}'

    @property
    def email(self):
        return f'{self._first_name.lower()}.{self._last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self._salary * self.TAX_RATE, 2)

    def apply_bonus(self):
        self._salary = int(self._salary * (1 + self.BONUS_RATE))

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
