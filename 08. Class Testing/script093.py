import unittest


class StringProcessor:
    def reverse_words(self, string):
        words = string.split()
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)


class TestStringProcessor(unittest.TestCase):
    def test_reverse_words(self):
        processor = StringProcessor()
        self.assertEqual(processor.reverse_words("hello world"), "olleh dlrow")
        self.assertEqual(processor.reverse_words("Python is fun"), "nohtyP si nuf")
        self.assertEqual(processor.reverse_words("reverse   spaces"), "esrever secaps")


if __name__ == "__main__":
    unittest.main()
