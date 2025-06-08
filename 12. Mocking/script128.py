import unittest
from unittest.mock import patch
from message_generator import get_message


class TestGetMessage(unittest.TestCase):
    @patch("get_today_name", return_value="Friday")
    def test_get_message_with_friday(self):
        actual = get_message()
        expected = "Hello Friday"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
