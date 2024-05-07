from account import Account
import unittest

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(100)
    def test_account_initialization(self):
        self.assertEqual(100, self.account.get_balance())
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(150, self.account.get_balance())
    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(50, self.account.get_balance())
    def test_withdraw_not_enough_funds(self):
        #self.account.withdraw(150)
        #self.assertEqual(-50, self.account.get_balance())
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    def test_depisit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)