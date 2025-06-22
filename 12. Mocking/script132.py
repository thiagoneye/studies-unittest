import unittest
from unittest.mock import patch
from employees import Programmer


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer()
        self.programmer.add_tech("python")
        self.programmer.add_tech("sql")
        self.programmer.add_tech("java")
        self.programmer.add_tech("c++")
        self.programmer.add_tech("aws")

    @patch.object(Programmer, "get_random_tech")
    def test_get_random_tech_mocked_python(self, mock_tech):
        mock_tech.return_value = "python"
        actual = self.programmer.get_random_tech()
        expected = "python"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
