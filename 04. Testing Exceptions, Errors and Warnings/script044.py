import unittest


def calculate_shipping_cost(weight, destination):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    if not isinstance(destination, str):
        raise TypeError("Destination must be a string")
    if not destination:
        raise ValueError("Destination cannot be empty")
    if destination.lower() == "usa":
        return 0
    if destination.lower() == "canada":
        return weight * 1.5
    if destination.lower() == "mexico":
        return weight * 2.0
    return weight * 5.0


class TestCalculateShippingCost(unittest.TestCase):
    def test_non_numeric_weight(self):
        with self.assertRaises(TypeError):
            calculate_shipping_cost("100", "canada")

    def test_non_positive_weight(self):
        with self.assertRaises(ValueError):
            calculate_shipping_cost(-50, "canada")

    def test_non_string_destination(self):
        with self.assertRaises(TypeError):
            calculate_shipping_cost(100, ["canada", "mexico"])

    def test_empty_destination(self):
        with self.assertRaises(ValueError):
            calculate_shipping_cost(100, "")


if __name__ == "__main__":
    unittest.main()
