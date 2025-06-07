import unittest
from animal import Cat, Dog


class TestCats(unittest.TestCase):
    def test_make_sound(self):
        cat = Cat("Whiskers")
        self.assertEqual(cat.make_sound(), "meow")
        self.assertNotEqual(cat.make_sound(), "woof")

    def test_species(self):
        cat = Cat("Whiskers")
        self.assertEqual(cat.species, "cat")


class TestDogs(unittest.TestCase):
    def test_make_sound(self):
        dog = Dog("Fido")
        self.assertEqual(dog.make_sound(), "woof")
        self.assertNotEqual(dog.make_sound(), "meow")

    def test_species(self):
        dog = Dog("Fido")
        self.assertEqual(dog.species, "dog")
