import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")

    def test_calculate_interest(self):
        self.assertEqual(self.account1.calculate_interest(), 15.0)
        self.assertEqual(self.account2.calculate_interest(), 7.5)
        self.account1.balance = 1500
        self.assertEqual(self.account1.calculate_interest(), 22.5)


if __name__ == "__main__":
    unittest.main()
