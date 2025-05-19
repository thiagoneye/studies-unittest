import random
import string
import unittest


def generate_password(n):
    password = "".join(
        random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n
        )
    )
    return password


class TestGeneratePassword(unittest.TestCase):
    def test_generate_password(self):
        password = generate_password(10)

        self.assertEqual(len(password), 10)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))


if __name__ == "__main__":
    unittest.main()
