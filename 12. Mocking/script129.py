import unittest
from unittest.mock import patch
from message_generator import get_message


class TestGetMessage(unittest.TestCase):
    @patch("message_generator.get_today_name")
    def test_get_message_with_friday(self, mock_day):
        mock_day.return_value = "Friday"
        actual = get_message()
        expected = "Hello Friday!"
        self.assertEqual(actual, expected)

    @patch("message_generator.get_today_name")
    def test_get_message_with_monday(self, mock_day):
        mock_day.return_value = "Monday"
        actual = get_message()
        expected = "Hello Monday!"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
