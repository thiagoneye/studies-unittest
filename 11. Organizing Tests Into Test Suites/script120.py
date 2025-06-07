import unittest
from test_animals import TestCats, TestDogs


if __name__ == "__main__":
    # Create test loaders and load test cases
    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromTestCase(TestCats)
    suite2 = loader.loadTestsFromTestCase(TestDogs)

    # Create a master test suite containing the individual test suites
    master_suite = unittest.TestSuite([suite1, suite2])

    # Create a test runner and run the suite
    runner = unittest.TextTestRunner()
    runner.run(master_suite)
