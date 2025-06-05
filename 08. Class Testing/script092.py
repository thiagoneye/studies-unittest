import unittest


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class TestShoppingCart(unittest.TestCase):
    def test_add_remove_item(self):
        cart = ShoppingCart()
        cart.add_item("apple")
        self.assertIn("apple", cart.items)

        cart.add_item("banana")
        self.assertIn("apple", cart.items)
        self.assertIn("banana", cart.items)

        cart.remove_item("apple")
        self.assertNotIn("apple", cart.items)

        cart.remove_item("banana")
        self.assertEqual(len(cart.items), 0)


if __name__ == "__main__":
    unittest.main()
