import unittest


class Pet:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name


class TestPet(unittest.TestCase):
    def test_pet_has_name_property(self):
        msg = "The Pet class does not have a name attribute."
        self.assertTrue(hasattr(Pet, "name"), msg)
        self.assertIsInstance(getattr(Pet, "name", None), property, msg)


if __name__ == "__main__":
    unittest.main()
