import unittest
from basket import ShoppingBasket


class TestBasketWithNoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)

    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0.0)


class TestBasketWithOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket().add_product(name="milk", price=3.0)

    def test_size_of_basket_should_be_one(self):
        actual = len(self.basket)
        expected = 1
        self.assertEqual(actual, expected)

    def test_total_amount_should_have_tax(self):
        actual = self.basket.total()
        expected = 3.63
        self.assertEqual(actual, expected)

    def test_getting_product(self):
        actual = self.basket.get_product(0).name
        expected = "milk"
        self.assertEqual(actual, expected)

    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(1)


class TestBasketWithTwoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = (
            ShoppingBasket()
            .add_product(name="milk", price=3.0)
            .add_product(name="water", price=2.0)
        )

    def test_size_of_basket_should_be_two(self):
        actual = len(self.basket)
        expected = 2
        self.assertEqual(actual, expected)

    def test_order_of_products(self):
        self.assertEqual(self.basket.get_product(0).name, "milk")
        self.assertEqual(self.basket.get_product(0).price, 3.0)
        self.assertEqual(self.basket.get_product(1).name, "water")
        self.assertEqual(self.basket.get_product(1).price, 2.0)

    def test_total_amount_should_have_tax(self):
        actual = self.basket.total()
        expected = 6.05
        self.assertEqual(actual, expected)

    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(2)


if __name__ == "__main__":
    unittest.main()
