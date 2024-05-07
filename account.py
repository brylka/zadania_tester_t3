class Account:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Cannot deposit a negative amount")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")
    def get_balance(self):
        return self.balance