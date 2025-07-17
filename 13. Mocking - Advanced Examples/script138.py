import unittest
from unittest.mock import MagicMock, patch
from my_module import fetch_data, get_average_value


class TestMyModule(unittest.TestCase):
    def test_fetch_data(self):
        # Mock the requests library to return a specific response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"value": 1},
            {"value": 2},
            {"value": 3},
        ]
        with patch("requests.get", return_value=mock_response):
            data = fetch_data()
        self.assertEqual(data, [{"value": 1}, {"value": 2}, {"value": 3}])

    def test_get_average_value(self):
        # Test with valid data
        data = [{"value": 1}, {"value": 2}, {"value": 3}]
        field = "value"
        result = get_average_value(data, field)
        self.assertEqual(result, 2)

        # Test with missing field
        data = [{"value": 1}, {"other_field": 2}, {"value": 3}]
        field = "value"
        result = get_average_value(data, field)
        self.assertEqual(result, 2)

        # Test with no data
        data = []
        field = "value"
        result = get_average_value(data, field)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
