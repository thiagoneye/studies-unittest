import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(1500)

    def test_transfer_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(1500, self.account2)


if __name__ == "__main__":
    unittest.main()
