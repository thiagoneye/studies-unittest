import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("123456", 1000, "checking", 500)
        self.account2 = BankAccount("654321", 500, "savings", 1000)

    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 1500)
        self.account2.deposit(1000)
        self.assertEqual(self.account2.balance, 1500)

    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 500)
        self.assertRaises(ValueError, self.account1.withdraw, 1500)
        self.account2.withdraw(1000)
        self.assertEqual(self.account2.balance, -500)

    def test_transfer(self):
        self.account1.transfer(500, self.account2)
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 1000)
        self.assertRaises(ValueError, self.account1.transfer, 1500, self.account2)
        self.account2.transfer(1500, self.account1)
        self.assertEqual(self.account1.balance, 2000)
        self.assertEqual(self.account2.balance, -500)


if __name__ == "__main__":
    unittest.main()
