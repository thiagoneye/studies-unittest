import unittest


def remove_vowels(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    vowels = ["a", "e", "i", "o", "u"]
    return "".join([char for char in input_str if char.lower() not in vowels])


class TestRemoveVowels(unittest.TestCase):
    def test_remove_vowels(self):
        test_cases = [
            ("hello world", "hll wrld"),
            ("Python is awesome", "Pythn s wsm"),
            ("aeiou", ""),
            ("", ""),
            (["not a string"], None),
            ({"not a string": "value"}, None),
            (None, None),
        ]

        for actual, expected in test_cases:
            with self.subTest(actual=actual, expected=expected):
                if not isinstance(actual, str):
                    with self.assertRaises(TypeError):
                        remove_vowels(actual)
                else:
                    self.assertEqual(remove_vowels(actual), expected)


if __name__ == "__main__":
    unittest.main()
