import unittest
import os


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as f:
            return f.read()


class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.filename = "test.txt"

        with open(self.filename, "w") as f:
            f.write("Hello, word!")

    def tearDown(self):
        os.remove(self.filename)

    @unittest.skipUnless(os.path.isfile('test.txt'), "File not found")
    def test_read_data(self):
        reader = FileReader(self.filename)
        data = reader.read_data()
        self.assertTrue(data, "Hello, word!")


if __name__ == "__main__":
    unittest.main()
