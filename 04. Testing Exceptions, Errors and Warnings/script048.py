import json
import unittest
import warnings


def parse_data(input_string):
    try:
        data = json.loads(input_string)
    except ValueError:
        warnings.warn("Invalid JSON string", category=Warning)
        return {}
    else:
        return data


class TestParseData(unittest.TestCase):
    def test_invalid_json_warning(self):
        with self.assertWarns(Warning):
            parse_data("123=456=789")
        with self.assertWarns(Warning):
            parse_data('{"name": "Alice", "age": 30, }')


if __name__ == "__main__":
    unittest.main()
