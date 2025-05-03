"""
An implementation of the StringListOnly class is given.

Only objects of type str can be added to the list of type StringListOnly using the append() method.

Using the unittest framework create a TestStringListOnly class that inherits from
the unittest.TestCase class that implements the test method:

- test_slo_is_instance()
    checks if instance slo = StringListOnly() is an instance of the StringListOnly class.
        Use the assertIsInstance() method.
    checks if instance slo = StringListOnly() is an instance of the list class.
        Use the assertIsInstance() method.

You only need to implement the class and the appropriate test methods.

During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.
"""

import unittest

class StringListOnly(list):
    def append(self, string: str) -> None:
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)

class TestStringListOnly(unittest.TestCase):
    def test_slo_is_instance(self):
        slo = StringListOnly()
        self.assertIsInstance(slo, StringListOnly)
        self.assertIsInstance(slo, list)

if __name__ == "__main__":
    unittest.main()
