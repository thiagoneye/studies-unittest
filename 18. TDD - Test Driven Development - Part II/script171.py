import unittest


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"


class TestVector(unittest.TestCase):
    def setUp(self):
        self.v = Vector(-3, 4, 2)

    def test_vector_repr_method(self):
        msg = "The __repr__() method is not implemented correctly."
        actual = repr(self.v)
        expected = "Vector(-3, 4, 2)"
        self.assertEqual(actual, expected, msg)


if __name__ == "__main__":
    unittest.main()
