class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name_TLD = account_name
        self.balance_TLD = balance

    def deposit(self, amount):
        self.balance_TLD += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance_TLD:
            self.balance_TLD -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance_TLD)


account = BankAccount("Juan", 5000)
account.deposit(1000)
account.withdraw(2000)
account.display_balance()
