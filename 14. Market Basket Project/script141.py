import unittest
from product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("milk", 3.0)

    def test_get_product_name(self):
        actual = self.product.name
        expected = "milk"
        self.assertEqual(actual, expected)

    def test_get_product_price(self):
        actual = self.product.price
        expected = 3.0
        self.assertEqual(actual, expected)

    def test_get_quantity(self):
        actual = self.product.quantity
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
