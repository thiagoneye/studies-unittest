import unittest
from unittest.mock import MagicMock, patch
from my_module import get_weather


class TestGetWeather(unittest.TestCase):
    @patch("requests.get")
    def test_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "London",
            "main": {"temp": 283.15, "humidity": 70},
            "weather": [{"description": "scattered clouds"}],
        }
        mock_get.return_value = mock_response

        result = get_weather("London,UK")

        self.assertEqual(result["location"], "London")
        self.assertEqual(result["temperature"], 283.15)
        self.assertEqual(result["weather_description"], "scattered clouds")
        self.assertEqual(result["humidity"], 70)
        mock_get.assert_called_once_with(
            "http://api.openweathermap.org/data/2.5/weather"
            "?q=London,UK&appid=<your API key>"
        )


if __name__ == "__main__":
    unittest.main()
