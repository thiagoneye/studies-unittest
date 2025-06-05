import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("Alice", 30, "Female")
        self.person2 = Person("Bob", 25, "Male")

    def test_person_attributes(self):
        self.assertEqual(self.person1.name, "Alice")
        self.assertEqual(self.person1.age, 30)
        self.assertEqual(self.person1.gender, "Female")

        self.assertEqual(self.person2.name, "Bob")
        self.assertEqual(self.person2.age, 25)
        self.assertEqual(self.person2.gender, "Male")

    def test_person_str_method(self):
        self.assertEqual(str(self.person1), "Alice (30, Female)")
        self.assertEqual(str(self.person2), "Bob (25, Male)")


if __name__ == "__main__":
    unittest.main()
