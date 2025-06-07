import unittest


def calculate_rectangle_area(length, width):
    return length * width


def calculate_square_area(side_length):
    return side_length**2


class TestAreaFunctions(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
        self.assertEqual(calculate_rectangle_area(3, 4), 12)

    def test_square_area(self):
        self.assertEqual(calculate_square_area(5), 25)
        self.assertEqual(calculate_square_area(2), 4)


if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()

    suite.addTest(TestAreaFunctions("test_rectangle_area"))
    suite.addTest(TestAreaFunctions("test_square_area"))

    # Create a test runner and run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
