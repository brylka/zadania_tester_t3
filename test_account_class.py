from account import Account
import unittest

class TestAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.account = Account(100)
    def test_1_account_initialization(self):
        self.assertEqual(100, self.account.get_balance())
    def test_2_deposit(self):
        self.account.deposit(50)
        self.assertEqual(150, self.account.get_balance())
    def test_3_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(100, self.account.get_balance())
    def test_4_withdraw_not_enough_funds(self):
        #self.account.withdraw(150)
        #self.assertEqual(-50, self.account.get_balance())
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    def test_5_depisit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

if __name__ == '__main__':
    unittest.main()