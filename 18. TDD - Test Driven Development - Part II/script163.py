import unittest


class Phone:
    brand = "Apple"
    model = "iPhone X"


class TestPhone(unittest.TestCase):
    def test_brand_attr(self):
        msg = "The brand attribute for the Phone class is missing."
        self.assertTrue(hasattr(Phone, "brand"), msg)

    def test_model_attr(self):
        msg = "The model attribute for the Phone class is missing."
        self.assertTrue(hasattr(Phone, "model"), msg)

    def test_check_user_defined_class_attr(self):
        msg = "Two Phone class attributes are not defined."
        actual = len([attr for attr in dir(Phone) if not attr.startswith("_")])
        expected = 2
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
