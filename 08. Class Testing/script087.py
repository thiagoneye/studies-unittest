import unittest
from notebook import Note


class TestNote(unittest.TestCase):
    def setUp(self):
        self.note = Note("Simple note.")

    def test_note_has_category_class_attr(self):
        msg = "The Note class does not have a CATEGORY attribute."
        self.assertTrue(hasattr(self.note, "CATEGORY"), msg)


if __name__ == "__main__":
    unittest.main()
