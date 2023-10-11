import datetime
from bisect import bisect_left


class InsufficientFundsException(Exception):

    """Raised when there are insufficient funds to withdraw from the account."""

    pass


class BankAccount:
    def __init__(self) -> None:
        self.transaction_history: list[tuple[float, datetime.datetime, float]] = []

    def deposit(self, amount: float, timestamp: datetime.datetime) -> None:
        if len(self.transaction_history) == 0:
            last_bal = 0
        else:
            last_bal = self.transaction_history[-1][2]
        self.transaction_history.append((amount, timestamp, last_bal + amount))

    def withdraw(self, amount: float, timestamp: datetime.datetime) -> None:
        # check if withdraw is possible (enough bal) or not
        if len(self.transaction_history) == 0:
            last_bal = 0
        else:
            last_bal = self.transaction_history[-1][2]

        if last_bal >= amount:
            self.transaction_history.append((-1 * amount, timestamp, last_bal - amount))
        else:
            raise InsufficientFundsException

    def show_balance_slow(self, timestamp: datetime.datetime) -> float:
        """
        traverse the t_history from left-> right
        dict key= dt, value= final balance at that dt
        list element= epoch (sorted because we only append)
        when retieving bal at epoch x
        8am, 9am
        8.30 ->  of this as key to search in dict
        for naive approach:
            latest_bal_calculation logic
            iterate list until element> 8.30:
                stop

        """
        bal = 0
        for t in self.transaction_history:
            if t[1] > timestamp:
                break
            bal += t[0]
        return bal

    def show_balance(self, timestamp: datetime.datetime) -> float:
        if len(self.transaction_history) == 0:
            return 0
        # add 1 micros so bisect will include transaction same time
        ts_extra = timestamp + datetime.timedelta(microseconds=1)
        left_nearest_dt = bisect_left(
            self.transaction_history, ts_extra, key=lambda x: x[1]
        )
        # -1 cause bisect_left return the index after the highest lower timestamp
        return self.transaction_history[left_nearest_dt - 1][2]


def main():
    account = BankAccount()
    # when
    account.deposit(amount=1_000.00, timestamp=datetime.datetime(2022, 5, 13, 12, 0, 0))
    account.deposit(amount=500.00, timestamp=datetime.datetime(2022, 5, 18, 13, 15, 0))
    account.withdraw(amount=700.00, timestamp=datetime.datetime(2022, 5, 20, 8, 30, 0))
    for t in account.transaction_history:
        print(t)
    print(account.show_balance(timestamp=datetime.datetime(2022, 5, 14, 0, 0, 0)))


if __name__ == "__main__":
    main()
