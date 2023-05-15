class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance


class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def execute(self):
        if self.from_account.balance < self.amount:
            raise ValueError("Insufficient funds")
        self.from_account.balance -= self.amount
        self.to_account.balance += self.amount


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account_by_number(from_account_number)
        to_account = self.get_account_by_number(to_account_number)
        transaction = Transaction(from_account, to_account, amount)
        transaction.execute()

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise ValueError("Account not found")
