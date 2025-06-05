import unittest
from products import Product


class TestProduct(unittest.TestCase):
    def test_product_has_private_generate_id_method(self):
        self.assertTrue(hasattr(Product, "_generate_id"))
        self.assertTrue(callable(Product._generate_id))


if __name__ == "__main__":
    unittest.main()
