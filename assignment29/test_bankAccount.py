import unittest
from bank_account import BankAccount

class testBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(99999999, "Tim", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(100), "Deposited $100. New balance: $200")
        self.assertEqual(self.account.deposit(-100), "Invalid amount for deposit.")
        self.assertEqual(self.account.deposit(0), "Invalid amount for deposit.")

    def test_displayBalance(self):
        self.assertEqual(self.account.display_balance(), "Current Balance: $100" )

    def test_withDraw(self):
        self.assertEqual(self.account.withdraw(50), "Withdrew $50. New balance: $50")
        self.assertEqual(self.account.withdraw(20), "Withdrew $20. New balance: $30")
        self.assertEqual(self.account.withdraw(0), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account.withdraw(-100), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account.withdraw(200), "Insufficient funds or invalid amount for withdrawal.")


if __name__ == "__main__":
    unittest.main()

