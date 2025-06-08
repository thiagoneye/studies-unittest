import unittest
from unittest.mock import patch
from code_generator import get_code


class TestGetCode(unittest.TestCase):
    @patch("random.randint", return_value=30)
    def test_get_code_mock_should_return_30(self, mocked_random):
        actual = get_code()
        expected = "CX-30"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
