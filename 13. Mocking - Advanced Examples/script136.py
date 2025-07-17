import unittest
from unittest.mock import MagicMock, patch
from my_module import get_content


class TestGetContent(unittest.TestCase):
    @patch("requests.get")
    def test_success(self, mock_get):
        mock_response = MagicMock(status_code=200, content=b"Hello, world!")
        mock_get.return_value = mock_response

        result = get_content("http://example.com")

        self.assertEqual(result, "Hello, world!")
        mock_get.assert_called_once_with("http://example.com")

    @patch("requests.get")
    def test_retry(self, mock_get):
        mock_response = MagicMock(status_code=500, content=b"Hello, world!")
        mock_get.side_effect = [Exception, Exception, mock_response]

        result = get_content("http://example.com")

        self.assertEqual(result, "Hello, world!")
        self.assertEqual(mock_get.call_count, 3)


if __name__ == "__main__":
    unittest.main()
