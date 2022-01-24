class BankAccount:
    all_accounts = []
    def __init__(self) -> None:
        pass
    def __init__(self, balance = 0, intRate = .01) -> None:
        self.Balance = balance
        self.intRate = intRate
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.Balance += amount
        return self
    def withdraw(self, amount):
        if (self.Balance > amount):
            self.Balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.Balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.Balance}")
        return self
    def yield_interest(self):
        int_payment = 0
        if self.Balance > 0:
            int_payment = (self.Balance * self.intRate)
            self.Balance += int_payment
            print(f"Making interest payment of ${int_payment}")
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Account balance: {account.Balance}, Interest rate: %{account.intRate * 100}")

account1 = BankAccount(4500, .05)
account2 = BankAccount(1877)
account3 = BankAccount()

account1.deposit(277).deposit(824).deposit(27.50).withdraw(84.50).yield_interest().display_account_info()
account2.deposit(844).deposit(627).withdraw(44).withdraw(987).withdraw(99).withdraw(143).yield_interest().display_account_info()
account3.withdraw(44.78)
BankAccount.print_all_accounts()

