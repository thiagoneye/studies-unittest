import unittest
from notebook import Notebook


class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()
        self.notebook.add_note("Big Data")
        self.notebook.add_note("Data Science")
        self.notebook.add_note("Machine Learning")

    def test_search_notes_method(self):
        actual = self.notebook.search_notes("data")
        expected = ["Big Data", "Data Science"]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
