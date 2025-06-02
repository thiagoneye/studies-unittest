import unittest
from notebook import Note


class TestNote(unittest.TestCase):
    def setUp(self):
        self.note = Note("Simple note.")

    def test_note_has_content_instance_attr(self):
        msg = "A Note instance does not have a content attribute."
        self.assertTrue(hasattr(self.note, "content"), msg)


if __name__ == "__main__":
    unittest.main()
