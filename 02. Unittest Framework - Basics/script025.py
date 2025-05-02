"""
Suppose you have the TemperatureConverter class with the celsius_to_fahrenheit method.

Create the unit test class named TestTemperatureConverter and define the test cases.

In the test_celsius_to_fahrenheit() method tests the celsius_to_fahrenheit() static
method of the TemperatureConverter class by creating a new instance of the class,
calling the celsius_to_fahrenheit() method with three different temperature values 
in Celsius, and checking that the return value matches the expected result using the
assertAlmostEqual() method.
"""

import unittest

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32

class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        converter = TemperatureConverter()
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(-3), 26.6, delta=0.5)
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(0), 32, delta=0.5)
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(10), 50, delta=0.5)

if __name__ == "__main__":
    unittest.main()
