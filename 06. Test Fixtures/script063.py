import unittest
import tempfile


class FileReader:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()


class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.file = tempfile.NamedTemporaryFile(mode="w", delete=False)
        self.file.write("Hello, world!")
        self.file.close()

    def tearDown(self):
        import os
        os.unlink(self.file.name)
    
    def test_read_file(self):
        reader = FileReader()
        actual = reader.read_file(self.file.name)
        expected = "Hello, world!"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
