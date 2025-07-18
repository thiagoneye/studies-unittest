import unittest


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError("The price attribute must be a positive int or float.")
        elif price <= 0:
            raise ValueError("The price attribute must be a positive int or float.")
        self.price = price


class TestLaptop(unittest.TestCase):
    def test_laptop_incorrect_price_should_raise_type_error(self):
        with self.assertRaises(TypeError):
            Laptop("Acer", "Predator", "thousand")
        with self.assertRaises(TypeError):
            Laptop("Acer", "Predator", [2000])
        with self.assertRaises(TypeError):
            Laptop("Acer", "Predator", None)

    def test_laptop_incorrect_price_should_raise_value_error(self):
        with self.assertRaises(ValueError):
            Laptop("Acer", "Predator", -1000)
        with self.assertRaises(ValueError):
            Laptop("Acer", "Predator", 0)


if __name__ == "__main__":
    unittest.main()
