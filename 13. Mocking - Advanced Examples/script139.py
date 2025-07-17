import unittest
from unittest import mock
from weather import WeatherAPI, WeatherAnalyzer


class TestWeatherAnalyzer(unittest.TestCase):
    def test_is_raining(self):
        # Mocking weather data
        weather_data = {"weather": [{"main": "Rain"}]}

        # Creating a mock weather API
        weather_api = mock.MagicMock(spec=WeatherAPI)
        weather_api.get_weather.return_value = weather_data

        # Creating a WeatherAnalyzer instance
        weather_analyzer = WeatherAnalyzer()
        result = weather_analyzer.is_raining(weather_data)

        # Asserting that the result is True
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
