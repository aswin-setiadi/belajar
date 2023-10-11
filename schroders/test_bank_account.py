import datetime
import unittest

from bank_account import BankAccount, InsufficientFundsException


class TestBankAccount(unittest.TestCase):
    """
    instantiate BankAccount
    deposit(val, deposite_dt)
    #it should keep total acc deposit balance
    #we withdraw 700 (left 800)
    # should raise insuff. when withdraw > total_deposit
    # when queried on given date, should reflect the total_deposit until that dt
    """

    def test_acceptance_criteria(self):
        # given
        account = BankAccount()
        # when
        account.deposit(
            amount=1_000.00, timestamp=datetime.datetime(2022, 5, 13, 12, 0, 0)
        )
        account.deposit(
            amount=500.00, timestamp=datetime.datetime(2022, 5, 18, 13, 15, 0)
        )
        account.withdraw(
            amount=700.00, timestamp=datetime.datetime(2022, 5, 20, 8, 30, 0)
        )
        # then
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(
                amount=1_000.00, timestamp=datetime.datetime(2022, 5, 20, 9, 0, 0)
            )
        self.assertEqual(
            1_000.00,
            account.show_balance(timestamp=datetime.datetime(2022, 5, 14, 0, 0, 0)),
        )
        self.assertEqual(
            1_500.00,
            account.show_balance(timestamp=datetime.datetime(2022, 5, 18, 13, 30, 0)),
        )
        self.assertEqual(
            800.00,
            account.show_balance(timestamp=datetime.datetime(2022, 5, 20, 8, 45, 0)),
        )
        self.assertEqual(
            800.00,
            account.show_balance(timestamp=datetime.datetime(2022, 5, 20, 9, 15, 0)),
        )

        self.assertEqual(
            800.00,
            account.show_balance(timestamp=datetime.datetime(2022, 5, 20, 8, 30, 0)),
        )


if __name__ == "__main__":
    unittest.main()
