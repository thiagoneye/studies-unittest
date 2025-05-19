import unittest


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
        
        
class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4.0))
        self.assertTrue(is_even(-2))

    def test_odd_numbers(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3.0))
        self.assertFalse(is_even(5.5))
        self.assertFalse(is_even(-1))


if __name__ == "__main__":
    unittest.main()
