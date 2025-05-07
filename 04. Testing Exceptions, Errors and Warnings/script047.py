import unittest
import warnings


class User:
    def __init__(self, password):
        self.password = password
        if len(password) < 8:
            warnings.warn("Password too short", category=Warning)


class TestUser(unittest.TestCase):
    def test_short_password_warning(self):
        with self.assertWarns(Warning):
            user = User("123")
        with self.assertWarns(Warning):
            user = User("1234567")


if __name__ == "__main__":
    unittest.main()
