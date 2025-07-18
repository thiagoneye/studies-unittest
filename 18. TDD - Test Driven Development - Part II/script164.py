import unittest


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class TestLaptop(unittest.TestCase):
    def setUp(self):
        self.laptop = Laptop("Acer", "Predator", 5490)

    def test_laptop_has_brand_instance_attr(self):
        msg = "brand instance attribute is missing."
        self.assertTrue(hasattr(self.laptop, "brand"), msg)

    def test_laptop_has_model_instance_attr(self):
        msg = "model instance attribute is missing."
        self.assertTrue(hasattr(self.laptop, "model"), msg)

    def test_laptop_has_price_instance_attr(self):
        msg = "price instance attribute is missing."
        self.assertTrue(hasattr(self.laptop, "price"), msg)

    def test_laptop_has_three_instance_attrs(self):
        msg = "Three instance attributes are not defined."
        actual = len([attr for attr in dir(self.laptop) if not attr.startswith("_")])
        expected = 3
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
