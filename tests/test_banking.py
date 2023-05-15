import unittest

from examples.banking import Bank, Account


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_add_account(self):
        account1 = Account(1, 100)
        account2 = Account(2, 200)
        self.bank.add_account(account1)
        self.bank.add_account(account2)
        self.assertEqual(len(self.bank.accounts), 2)

    def test_transfer(self):
        account1 = Account(1, 100)
        account2 = Account(2, 200)
        self.bank.add_account(account1)
        self.bank.add_account(account2)
        self.bank.transfer(1, 2, 50)
        self.assertEqual(account1.balance, 50)
        self.assertEqual(account2.balance, 250)

    def test_transfer_insufficient_funds(self):
        account1 = Account(1, 100)
        account2 = Account(2, 200)
        self.bank.add_account(account1)
        self.bank.add_account(account2)
        with self.assertRaises(ValueError):
            self.bank.transfer(1, 2, 150)

    def test_get_account_by_number(self):
        account1 = Account(1, 100)
        account2 = Account(2, 200)
        self.bank.add_account(account1)
        self.bank.add_account(account2)
        result = self.bank.get_account_by_number(1)
        self.assertEqual(result, account1)


if __name__ == '__main__':
    unittest.main()
