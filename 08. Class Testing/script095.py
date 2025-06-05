import unittest
from shopping_cart import Item, ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.item1 = Item("Book", 15)
        self.item2 = Item("Shoes", 50)

    def test_add_item(self):
        self.cart.add_item(self.item1)
        self.assertIn(self.item1, self.cart.items)
        self.assertEqual(len(self.cart.items), 1)

        self.cart.add_item(self.item2)
        self.assertIn(self.item2, self.cart.items)
        self.assertEqual(len(self.cart.items), 2)

    def test_remove_item(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.cart.remove_item(self.item1)
        self.assertNotIn(self.item1, self.cart.items)
        self.assertEqual(len(self.cart.items), 1)

    def test_get_total_price(self):
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)
        self.assertEqual(self.cart.get_total_price(), 65)


if __name__ == "__main__":
    unittest.main()
