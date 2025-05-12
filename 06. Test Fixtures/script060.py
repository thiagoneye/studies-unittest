import sys
import unittest


class Container:
    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Container(category='{self.category}')"


class TestContainer(unittest.TestCase):
    def setUp(self):
        self.container = Container('plastic')

    def test_init_method(self):
        msg = ('The container instance does not have a category attribute.')
        self.assertTrue(hasattr(self.container, 'category'), msg)
        self.assertEqual(self.container.category, 'plastic')

    def test_repr_method(self):
        self.assertEqual(repr(self.container), "Container(category='plastic')")


if __name__ == "__main__":
    unittest.main()
