import unittest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def tearDown(self):
        del self.calculator

    def test_add(self):
        actual = self.calculator.add(1, 2)
        expected = 3
        self.assertEqual(actual, expected)
    
    def test_subtract(self):
        actual = self.calculator.subtract(1, 2)
        expected = -1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
