import unittest


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("John", "Smith")

    def test_person_repr_method(self):
        msg = "The __repr__() method is not implemented correctly."
        actual = repr(self.person)
        expected = f"Person(fname='{self.person.fname}', lname='{self.person.lname}')"
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
