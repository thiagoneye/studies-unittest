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

    def test_repr_method(self):
        self.assertEqual(
            repr(self.product),
            "Product(name='milk', price=3.0, quantity=1)",
            "Product's __repr__ method did not return expected result",
        )


if __name__ == "__main__":
    unittest.main()
