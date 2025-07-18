import string
import random


def generate_password():
    while True:
        password = "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=12,
            )
        )
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password


def test_generate_password():
    password = generate_password()
    assert len(password) >= 8
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)
