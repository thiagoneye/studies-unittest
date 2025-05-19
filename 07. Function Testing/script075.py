import unittest


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    return True


class TestIsValidPassword(unittest.TestCase):
    def test_is_valid_password_valid(self):
        self.assertTrue(is_valid_password("123456Pw"))

    def test_is_valid_password_short(self):
        self.assertFalse(is_valid_password("1234Pw"))

    def test_is_valid_password_no_digits(self):
        self.assertFalse(is_valid_password("QWERtyui"))

    def test_is_valid_password_no_uppercase(self):
        self.assertFalse(is_valid_password("12qwerty"))

    def test_is_valid_password_no_lowercase(self):
        self.assertFalse(is_valid_password("12QWERTY"))


if __name__ == "__main__":
    unittest.main()
