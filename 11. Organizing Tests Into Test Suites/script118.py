import unittest


def reverse_string(string):
    return string[::-1]


def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for letter in string:
        if letter.lower() not in vowels:
            result += letter
    return result


def capitalize_first_letter(string):
    return string.capitalize()


class TestStringManipulationFunctions(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("hello world"), "hll wrld")
        self.assertEqual(remove_vowels("python is awesome"), "pythn s wsm")

    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter("hello"), "Hello")
        self.assertEqual(capitalize_first_letter("world"), "World")


if __name__ == "__main__":
    # Create a test suite
    suite = unittest.TestSuite()

    suite.addTest(TestStringManipulationFunctions("test_reverse_string"))
    suite.addTest(TestStringManipulationFunctions("test_remove_vowels"))
    suite.addTest(TestStringManipulationFunctions("test_capitalize_first_letter"))

    # Create a test runner and run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
