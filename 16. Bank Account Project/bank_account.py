class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def transfer(self, amount, account):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        account.deposit(amount)

    def calculate_interest(self):
        return round(self.balance * 0.015, 2)
