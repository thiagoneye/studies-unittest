import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")

    def test_deposit(self):
        self.account1.deposit(1000)
        actual = self.account1.balance
        expected = 2000
        self.assertEqual(actual, expected)

    def test_withdraw(self):
        self.account1.withdraw(500)
        actual = self.account1.balance
        expected = 500
        self.assertEqual(actual, expected)

    def test_transfer(self):
        self.account1.transfer(500, self.account2)
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 1000)


if __name__ == "__main__":
    unittest.main()
