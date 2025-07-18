import unittest


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model

        if not isinstance(price, (int, float)):
            raise TypeError("The price attribute must be a positive int or float.")
        self.price = price


class TestLaptop(unittest.TestCase):
    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop, "Acer", "Predator", "thousand")
        self.assertRaises(TypeError, Laptop, "Acer", "Predator", [2000])
        self.assertRaises(TypeError, Laptop, "Acer", "Predator", None)


if __name__ == "__main__":
    unittest.main()
